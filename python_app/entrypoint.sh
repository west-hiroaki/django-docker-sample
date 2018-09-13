#!/bin/bash
set -e

# Djangoプロセス起動
# 注意）`python manage.py runserver` だと `127.0.0.1:8000` がbindアドレスとして登録されるため、コンテナ外からアクセスできない
python manage.py runserver 0.0.0.0:8000 >> /tmp/django.log &

/bin/bash --login
