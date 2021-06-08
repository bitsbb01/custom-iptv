#!/bin/bash
commit_time=$(date '+%Y-%m-%d-%H')
/usr/bin/python make_playlist.py >> make.log
git add -A
git commit -m "automatic update ${commit_time}"
git push
