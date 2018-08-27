#!/bin/bash

DB_HOST="127.0.0.1"
DB_NAME="sample"
DB_USER="root"
DB_PORT="3336"

R=`echo "DROP DATABASE IF EXISTS ${DB_NAME}; CREATE DATABASE ${DB_NAME} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -h${DB_HOST} -u${DB_USER} -P${DB_PORT}`
if [ ! "${R}" ]; then
    exit 1
fi

echo 'done.'

