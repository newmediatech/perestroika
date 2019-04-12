#!/usr/bin/env bash

export PYTHONPATH="$(pwd)"/perestroika:$PYTHONPATH
export PYTHONPATH="$(pwd)"/tests:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=tests.config.settings
python ./tests/manage.py migrate
coverage run --source='./perestroika/' -m pytest tests -vv && coverage combine && coverage report
