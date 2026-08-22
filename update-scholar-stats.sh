#!/usr/bin/env bash
# Refreshes Google Scholar citation data for xuhaolei.github.io.
# Runs the repo's crawler locally (GitHub Actions runner IPs are blocked by
# Scholar), pushes results to the google-scholar-stats branch, and purges the
# jsDelivr cache the site reads from.
#
# Install (every 2 days at 03:17):
#   17 3 */2 * * /home/devdesk/Desktop/personal_page/xuhaolei.github.io/update-scholar-stats.sh
# Log: ~/.cache/scholar-stats/update.log
set -euo pipefail

REPO_SSH22="git@github.com:xuhaolei/xuhaolei.github.io.git"
REPO_SSH443="ssh://git@ssh.github.com:443/xuhaolei/xuhaolei.github.io.git"
WORK="$HOME/.cache/scholar-stats"
LOG="$WORK/update.log"
export GIT_SSH_COMMAND="ssh -o BatchMode=yes -o ConnectTimeout=20 -o StrictHostKeyChecking=accept-new"

mkdir -p "$WORK"
exec >>"$LOG" 2>&1
echo "=== $(date -Is) ==="

# Pick a reachable GitHub SSH endpoint: port 22 first, then 443 (port 22 is
# occasionally refused from this host).
REPO=""
for candidate in "$REPO_SSH22" "$REPO_SSH443"; do
  if git ls-remote -q --exit-code "$candidate" HEAD >/dev/null 2>&1; then
    REPO="$candidate"
    break
  fi
done
if [ -z "$REPO" ]; then
  echo "GitHub unreachable over SSH (ports 22 and 443); will retry next run."
  exit 0
fi
echo "Using remote: $REPO"

sync_clone() {  # $1 = dir, $2 = branch
  if [ ! -d "$1/.git" ]; then
    git clone --depth 1 --branch "$2" "$REPO" "$1"
  else
    git -C "$1" remote set-url origin "$REPO"
    git -C "$1" pull -q --ff-only
  fi
}
sync_clone "$WORK/repo" master
sync_clone "$WORK/stats" google-scholar-stats

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
