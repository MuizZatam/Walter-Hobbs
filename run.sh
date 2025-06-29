#!/bin/bash

LOG_DIR="$HOME/walter_logs"
mkdir -p "$LOG_DIR"

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_FILE="$LOG_DIR/log_$TIMESTAMP.txt"

# Update the path to your virtualenv and Python script
source .venv/bin/activate
python3 src/main.py >> "$LOG_FILE" 2>&1 &

