DOCKER_COMPOSE = docker-compose -p myapp

# 環境初期化
init: build init_db migrate createsuperuser

build:
	$(DOCKER_COMPOSE) build

# DB再作成
init_db:
	$(DOCKER_COMPOSE) run --rm python_app mysql -hmysql -uroot -e'DROP DATABASE IF EXISTS sample;CREATE DATABASE sample DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;'

migrate:
	$(DOCKER_COMPOSE) run --rm python_app python manage.py migrate

createsuperuser:
	$(DOCKER_COMPOSE) run --rm python_app python manage.py createsuperuser

# Djangoサーバ起動
run: up runserver

up:
	$(DOCKER_COMPOSE) up -d

runserver:
    # 注意）`python manage.py runserver` だと `127.0.0.1:8000` がbindアドレスとして登録されるため、コンテナ外からアクセスできない
	$(DOCKER_COMPOSE) exec python_app python manage.py runserver 0:8000

ps:
	$(DOCKER_COMPOSE) ps

down:
	$(DOCKER_COMPOSE) down

stop:
	$(DOCKER_COMPOSE) stop

logs:
	$(DOCKER_COMPOSE) logs

# pythonアプリコンテナにbash接続
bash:
	$(DOCKER_COMPOSE) exec python_app bash
