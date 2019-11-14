# project/app/tasks.py

import os
from time import sleep

import celery
import redis

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

app = celery.Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)
cache = redis.Redis(host='redis', port=6379)

@app.task
def fib(num):
    '''Return a fibonacci sequence value of num'''
    # simulate slow computation
    # sleep(2)

    cached_result = cache.get(f'fib_{num}')
    if cached_result:
        return int(cached_result)

    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1

    result = fib(num - 2) + fib(num - 1)
    cache.set(f'fib_{num}', result)
    return result

