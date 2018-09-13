FROM python:3.4

RUN apt-get update
RUN apt-get install -y mysql-client

# ポート解放（docker-compose.ymlでフォワードしているポートは不要）
# EXPOSE 8000

# ユーザー追加
RUN useradd -m -s /bin/bash docker
# パスワード設定
RUN echo "docker:docker" | chpasswd
# sudo権限付与
RUN echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/docker
RUN chmod -R 777 /home/docker

## for python2
# ARG sitecustomize_file="/usr/local/lib/python2.7/site-packages/sitecustomize.py"
# RUN touch ${sitecustomize_file}
# RUN echo "import sys; sys.setdefaultencoding('utf-8')" > ${sitecustomize_file}

# pip install
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /home/docker/my_app

## ENTRYPOINT設定。ENTRYPOINTから runserver 起動させることも可能だったが、`docker-compose run` コマンドが実行できなくなるのでやめる
# COPY entrypoint.sh /sbin/entrypoint.sh
# RUN chmod 755 /sbin/entrypoint.sh
# ENTRYPOINT ["/sbin/entrypoint.sh"]
