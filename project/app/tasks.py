# project/app/tasks.py

import os
from time import sleep

import celery
import redis

from sympy import (
    symbols,
    sqrt,
    simplify,
)

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

app = celery.Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)
cache = redis.Redis(host='redis', port=6379)


@app.task
def fib(val):
    '''Return a fibonacci sequence value of num'''
    # simulate slow computation
    sleep(10)
    cached_result = cache.get(f'fib_{val}')
    if cached_result:
        return str(cached_result)

    n = symbols('n', integer=True)
    phi = (1+sqrt(5))/2
    f = (phi**n -(-phi)**(-n))/sqrt(5)

    fn = f.subs(n, val)
    result = f'{simplify(fn)}'
    cache.set(f'fib_{val}', result)
    return result
