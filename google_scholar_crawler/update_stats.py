"""Refreshes Google Scholar citation data from this (Windows) machine.

GitHub Actions runner IPs are blocked by Scholar, so a local scheduled task
runs this instead: crawl with main.py, push the JSON to the
google-scholar-stats branch, and purge the jsDelivr cache the site reads from.

Register the daily task (once):
  powershell -ExecutionPolicy Bypass -File google_scholar_crawler\\register_task.ps1
Log: %LOCALAPPDATA%\\scholar-stats\\update.log
"""
import json
import os
import shutil
import subprocess
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

SCHOLAR_ID = "Wg2cuHUAAAAJ"
REPO = "git@github.com:xuhaolei/xuhaolei.github.io.git"
BRANCH = "google-scholar-stats"
FILES = ["gs_data.json", "gs_data_shieldsio.json"]
CRAWLER = Path(__file__).resolve().parent / "main.py"
WORK = Path(os.environ.get("LOCALAPPDATA", Path.home())) / "scholar-stats"
LOG = WORK / "update.log"


def log(msg):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def git(*args, cwd=None):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


def load(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def main():
    stats = WORK / "stats"
    if (stats / ".git").exists():
        git("fetch", "-q", "--depth", "1", "origin", BRANCH, cwd=stats)
        git("reset", "-q", "--hard", f"origin/{BRANCH}", cwd=stats)
    else:
        git("clone", "-q", "--depth", "1", "--branch", BRANCH, REPO, str(stats))

    run_dir = WORK / "run"
    shutil.rmtree(run_dir / "results", ignore_errors=True)
    run_dir.mkdir(exist_ok=True)
    r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(CRAWLER)], cwd=run_dir,
                       env={**os.environ, "GOOGLE_SCHOLAR_ID": SCHOLAR_ID},
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    log(r.stdout.strip() + r.stderr.strip())

    # main.py exits 0 without writing results when Scholar blocks the request
    new = load(run_dir / "results" / "gs_data.json")
    if not new:
        log("No new data (blocked or empty response), keeping existing.")
        return

    old = load(stats / "gs_data.json") or {}
    # A partially rendered page can drop papers; never overwrite good data with it.
    if len(new["publications"]) < len(old.get("publications", {})) or \
            new["citedby"] < old.get("citedby", 0) * 0.9:
        log(f"Suspicious drop ({old.get('citedby')} -> {new['citedby']} citations, "
            f"{len(old.get('publications', {}))} -> {len(new['publications'])} papers), skipped.")
        return
    if {**new, "updated": None} == {**old, "updated": None}:
        log("No citation changes.")
        return

    for name in FILES:
        shutil.copy(run_dir / "results" / name, stats / name)
    git("-c", "user.name=Haolei Xu", "-c", "user.email=1215480959@qq.com",
        "commit", "-q", "-m", f"Updated Citation Data ({new['citedby']})", *FILES, cwd=stats)
    git("push", "-q", "origin", BRANCH, cwd=stats)
    for name in FILES:
        try:
            urllib.request.urlopen(f"https://purge.jsdelivr.net/gh/xuhaolei/xuhaolei.github.io@{BRANCH}/{name}", timeout=30)
        except OSError:
            pass
    log(f"Pushed updated citation data: {old.get('citedby')} -> {new['citedby']}.")


if __name__ == "__main__":
    WORK.mkdir(parents=True, exist_ok=True)
    log(f"=== {datetime.now().isoformat(timespec='seconds')} ===")
    try:
        main()
    except Exception as e:
        log(f"[error] {e}")
        sys.exit(1)
