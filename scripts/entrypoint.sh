#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python root.py wait_for_db
python root.py collectstatic --noinput
python root.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi