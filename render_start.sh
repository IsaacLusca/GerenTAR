#!/usr/bin/env bash
set -e

export FLASK_APP=scripts.py

flask db upgrade
flask seed

exec gunicorn app:app --bind 0.0.0.0:${PORT:-8000}
