#!/usr/bin/env bash
set -e

python startup.py

exec gunicorn app:app --bind 0.0.0.0:${PORT:-8000}
