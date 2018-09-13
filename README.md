# 目的
Django2.0 が動く環境を Docker 構成で作成。

* Python 3.4.0   
* Django 2.0.0
* MySQL 5.6

# 動作確認手順

必要なコマンドは Makefile にまとめています。

1. 環境生成  
`$ make init`  
Docker コンテナの生成・DBの構築を行います。  
途中で Django Admin の管理者ID、パスワード入力を求められます。

1. Django起動  
`$ make run`   
python_appコンテナ上のDjangoを起動（runserver）します。

1. 動作確認  
ローカルのブラウザで、`http://127.0.0.1:8888/admin` にアクセスします。
Django のログイン画面が表示されたら成功です。

# Djangoサンプルアプリ構成

1. プロジェクト追加  
`$ django-admin startproject sample_project`

1. アプリ追加  
`$ django-admin startapp sample_app`

1. モデルを追加し、migrate ファイルを生成  
`$ python manage.py makemigrations`

# MySQL接続コマンド

コンテナの MySQL に接続したい場合、以下のコマンドで行えます。
```
$ mysql -h127.0.0.1 -uroot -P3336
```
