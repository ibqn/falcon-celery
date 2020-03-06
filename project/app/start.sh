#!/bin/sh

if [[ ! -z $DEBUG ]]
 then
    RELOAD="--reload"
else
    RELOAD=""
fi

exec gunicorn app:app \
    --bind 0.0.0.0:8000 \
    --access-logfile=- \
    --workers 2 \
    ${RELOAD}
