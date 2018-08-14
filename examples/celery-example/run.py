from flask import Flask, request

import tasks
from metadata_logger import set_current_metadata
from metadata_logger.context.flask import init_metadata_logger

app = Flask(__name__)

# Initliase the metadata_logger Flask extension
init_metadata_logger()


@app.route('/')
def index():
    set_current_metadata({'username': request.args.get('username')})
    app.logger.warning("Metadata set! Sending a task...")
    tasks.app.send_task('examples.celery-example.tasks.log_username')
    return "success"


if __name__ == '__main__':
    with app.test_client() as c:
        c.get('/?username=batman')
