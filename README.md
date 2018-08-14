# metadata_logger

## Overview
A small library that allows arbitrary metadata to be automatically logged and passed around different contexts (e.g. Flask, Celery).
Heavily based on https://github.com/Workable/flask-log-request-id

## Examples
Some simple examples can be found in the `examples` directory.

To install the dependencies, run:
```
$ pipenv install
```

### Flask
```
$ pipenv run python examples/flask-example/app.py
```

### Flask to Celery
Celery needs a broker running. The example uses Redis, so it needs to be running on your system.

Start a worker:
```
$ pipenv run celery -A examples.celery-example.tasks worker
```

Submit a task:
```
$ pipenv run python examples/celery-example/run.py
```