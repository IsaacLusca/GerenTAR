#!/usr/bin/env bash
set -e

export FLASK_APP=scripts.py

flask db upgrade 2>/dev/null || flask db init && flask db migrate -m "initial" && flask db upgrade
flask seed

gunicorn app:app
