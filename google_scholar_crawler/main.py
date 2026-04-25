import json
import os
import time
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


class BlockedError(Exception):
    """Google Scholar blocked the request (403 / CAPTCHA). Caller should skip gracefully."""


def fetch_profile(scholar_id: str, max_attempts: int = 3):
    url = (
        f"https://scholar.google.com/citations"
        f"?user={scholar_id}&hl=en&sortby=pubdate&pagesize=100"
    )
    last_err = None
    for attempt in range(1, max_attempts + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            if resp.status_code == 403:
                raise BlockedError("403 Forbidden — Google Scholar blocked this IP")
            resp.raise_for_status()
            if "g-recaptcha" in resp.text or "please show you're not a robot" in resp.text.lower():
                raise BlockedError("CAPTCHA — Google Scholar blocked this IP")
            return resp.text
        except BlockedError:
            raise
        except Exception as exc:
            last_err = exc
            if attempt < max_attempts:
                time.sleep(5 * attempt)
    raise RuntimeError(f"Failed to fetch profile after {max_attempts} attempts: {last_err}")


def parse_profile(html: str, scholar_id: str):
    soup = BeautifulSoup(html, "html.parser")

    # Total citations (first gsc_rsb_std cell)
    total_cells = soup.find_all("td", class_="gsc_rsb_std")
    total_citations = int(total_cells[0].text.strip()) if total_cells else 0

    publications = {}
    for row in soup.find_all("tr", class_="gsc_a_tr"):
        title_el = row.find("a", class_="gsc_a_at")
        cite_el = row.find("a", class_="gsc_a_ac")
        year_el = row.find("span", class_="gsc_a_h")

        if not title_el:
            continue

        href = title_el.get("href", "")
        pub_id = href.split("citation_for_view=")[-1] if "citation_for_view=" in href else ""

        cite_count = 0
        cite_url = ""
        if cite_el:
            cite_text = cite_el.text.strip()
            cite_count = int(cite_text) if cite_text.isdigit() else 0
            raw_href = cite_el.get("href", "")
            if raw_href:
                cite_url = "https://scholar.google.com/" + raw_href.lstrip("/")

        pub = {
            "author_pub_id": pub_id,
            "bib": {"title": title_el.text.strip()},
            "num_citations": cite_count,
            "cite_url": cite_url,
        }
        if year_el:
            pub["bib"]["pub_year"] = year_el.text.strip()

        if pub_id:
            publications[pub_id] = pub

    return total_citations, publications


def main():
    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
    print(f"Fetching Google Scholar profile for {scholar_id}...")

    html = fetch_profile(scholar_id)
    total_citations, publications = parse_profile(html, scholar_id)

    print(f"Total citations: {total_citations}")
    print(f"Publications found: {len(publications)}")
    for pub in publications.values():
        title = pub["bib"].get("title", "?")[:60]
        print(f"  {pub['num_citations']:4d}  {title}")

    data = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "citedby": total_citations,
        "publications": publications,
    }

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(total_citations),
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as f:
        json.dump(shieldio_data, f, ensure_ascii=False)

    print("Done.")


if __name__ == "__main__":
    try:
        main()
    except BlockedError as e:
        print(f"[skip] {e}")
        print("Google Scholar blocked this runner's IP. Keeping existing data unchanged.")
        raise SystemExit(0)
