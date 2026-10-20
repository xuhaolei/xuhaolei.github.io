# xuhaolei.github.io

Personal homepage of Haolei Xu, built on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template. Content lives in `_pages/about.md`.

## Citation counts

Citation badges are filled in client-side from `gs_data.json` on the `google-scholar-stats` branch (via jsDelivr).

Google Scholar blocks GitHub Actions runner IPs, so the data is refreshed by a daily Windows scheduled task (`ScholarCitationUpdate`) on a local machine:

- `google_scholar_crawler/main.py` scrapes the Scholar profile.
- `google_scholar_crawler/update_stats.py` runs the crawler, pushes changed data to `google-scholar-stats`, and purges the jsDelivr cache. It skips the update when Scholar blocks the request or the result looks truncated.
- `google_scholar_crawler/register_task.ps1` registers the scheduled task (run once).

Log: `%LOCALAPPDATA%\scholar-stats\update.log`. Requires `pip install -r google_scholar_crawler/requirements.txt` and GitHub SSH access.

## Running locally

```
bundle install
bundle exec jekyll serve -l -H localhost
```
