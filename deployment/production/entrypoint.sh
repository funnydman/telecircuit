#!/usr/bin/env bash
set -e

PYTHON_INTERPRETER=$(which python3)
APPLICATION_ADDRESS=0.0.0.0
APPLICATION_PORT=8000

PATH_TO_STATIC_DIRECTORY=$(pwd)/telecircuit-manager/dist

function waiting_for_database {
    echo "Waiting for database."
    until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST_NAME" -U "$POSTGRES_USER" -c '\q'; do
      >&2 echo "Postgres is unavailable - sleeping."
      sleep 1
    done
    >&2 echo "Postgres is up - executing command."

}

function run_migrations {
    echo "Running database migrations."
    $PYTHON_INTERPRETER manage.py migrate --noinput --verbosity 0
}

function check_static_files {
    echo "CHECK STATIC files"
    while [ ! -d "$PATH_TO_STATIC_DIRECTORY" ]
    do
      echo "STATIC FILES IS UNAVAILABLE. WAITING!"
      sleep 5
    done
}
function collect_static {
    echo "Collecting application static files."
    $PYTHON_INTERPRETER manage.py collectstatic --noinput --verbosity 0
}

function run_tests {
    echo "Running tests."
    $PYTHON_INTERPRETER manage.py test
}

function run_server {
    echo "Running gunicorn."
    gunicorn telecircuit.wsgi -b $APPLICATION_ADDRESS:$APPLICATION_PORT
}


function main() {
    waiting_for_database
    run_migrations
    check_static_files
    collect_static
    run_tests
    run_server
}

main