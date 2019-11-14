# Falcon + Celery

Example of how to handle background processes with Falcon, Celery, and Docker

### Quick Start

Spin up the containers:

```sh
$ bash docker-compose.bash up --build
```

Open your browser to http://localhost:8000/ping to view the app or to http://localhost:5555 to view the Flower dashboard.

Redis-cli can be accessed by running

```sh
bash docker-compose.bash  run redis redis-cli -h redis
```

Trigger a new task:

```sh
 http --json :8000/create 'number=1000'
```
or with `curl`

```sh
$ curl -X POST http://localhost:8000/create \
    -d '{"number":"3"}' \
    -H "Content-Type: application/json"
```

Check the status:

```sh
http --json :8000/status/<ADD_TASK_ID>

```

or by

```sh
$ curl http://localhost:8000/status/<ADD_TASK_ID>
```

### Want to learn how to build this?

Check out the [post](https://testdriven.io/asynchronous-tasks-with-falcon-and-celery).
