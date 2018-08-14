
from celery import Celery

from metadata_logger import get_current_metadata, set_current_metadata
from metadata_logger.context.celery import enable_context_metadata_propagation

app = Celery('tasks', broker='redis://')
app.conf.worker_hijack_root_logger = False

# Initialise the metadata_logger Celery extension
enable_context_metadata_propagation()


@app.task
def log_username():
    print("Initial metadata: %s" % (get_current_metadata(),))
    print("Setting metadata...")
    set_current_metadata({'city': 'Gotham', **get_current_metadata()})
    print("Current metadata: %s" % (get_current_metadata(),))
    log_city.delay()


@app.task
def log_city():
    print("IN LOG TASK")
    print("Current metadata: %s" % (get_current_metadata(),))
