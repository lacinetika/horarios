#!/usr/bin/env bash
# Actual script directory path
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
. $DIR/venv/bin/activate
nohup python $DIR/main.py >> $DIR/output.log 2>&1 &