#!/usr/bin/env bash
# Refreshes Google Scholar citation data for xuhaolei.github.io.
# Runs the repo's crawler locally (GitHub Actions runner IPs are blocked by
# Scholar), pushes results to the google-scholar-stats branch, and purges the
# jsDelivr cache the site reads from. Installed in crontab (every 2 days).
set -euo pipefail

REPO=git@github.com:xuhaolei/xuhaolei.github.io.git
WORK="$HOME/.cache/scholar-stats"
LOG="$WORK/update.log"

mkdir -p "$WORK"
exec >>"$LOG" 2>&1
echo "=== $(date -Is) ==="

if [ ! -d "$WORK/repo" ]; then
  git clone --depth 1 "$REPO" "$WORK/repo"
else
  git -C "$WORK/repo" pull --ff-only
fi

if [ ! -d "$WORK/stats" ]; then
  git clone --depth 1 --branch google-scholar-stats "$REPO" "$WORK/stats"
else
  git -C "$WORK/stats" pull --ff-only
fi

cd "$WORK/repo/google_scholar_crawler"
rm -rf results
GOOGLE_SCHOLAR_ID=Wg2cuHUAAAAJ python3 main.py

# main.py exits 0 without writing results when Scholar blocks the request
if [ ! -f results/gs_data.json ]; then
  echo "No new data (blocked or empty response), keeping existing."
  exit 0
fi

cp results/gs_data.json results/gs_data_shieldsio.json "$WORK/stats/"
cd "$WORK/stats"
git config user.name "Haolei Xu"
git config user.email "1215480959@qq.com"
git add gs_data.json gs_data_shieldsio.json

if git diff --cached --quiet; then
  echo "No citation changes."
  exit 0
fi

git commit -m "Updated Citation Data"
git push origin google-scholar-stats
curl -fsS "https://purge.jsdelivr.net/gh/xuhaolei/xuhaolei.github.io@google-scholar-stats/gs_data.json" >/dev/null || true
curl -fsS "https://purge.jsdelivr.net/gh/xuhaolei/xuhaolei.github.io@google-scholar-stats/gs_data_shieldsio.json" >/dev/null || true
echo "Pushed updated citation data."
