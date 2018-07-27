#!/bin/bash
# Accepts one parameter:
# development
# or
# production
export FLASK_APP=news2vec
export FLASK_ENV=$1
flask run --host=0.0.0.0 --port=8889
