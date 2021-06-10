#!/bin/bash
commit_time=$(date '+%Y-%m-%d-%H')
cd /home/ted/custom-iptv/
/usr/bin/python make_playlist.py >> make.log
git add -A
git commit -m "automatic update ${commit_time}"
git push
