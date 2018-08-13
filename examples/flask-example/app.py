import logging

from flask import Flask, request
from flask.logging import default_handler

from metadata_logger import set_current_metadata
from metadata_logger.context.flask import init_metadata_logger
from metadata_logger.filter import MetadataLogFilter


class AddUsernameFormatter(logging.Formatter):
    def format(self, record):
        msg = "[{0}] {1}".format(record.levelname, record.getMessage())
        username = getattr(record, 'username', None)
        if username:
            msg += " '{0}'".format(username)
        return msg


def nananana(logger):
    logger.warning("nananana")


app = Flask(__name__)
app.logger.addFilter(MetadataLogFilter())
default_handler.setFormatter(AddUsernameFormatter())
app.logger.setLevel(logging.INFO)

init_metadata_logger()


@app.route('/')
def index():
    username = request.args.get('username')

    app.logger.info("This log statement uses 'extra'. Username is:", extra={'username': username})

    app.logger.info("Next, going to call a function and the username will be automatically logged")

    # after calling set_current_metadata, you can use get_current_metadata to get it back
    set_current_metadata({'username': username})
    app.logger.info("Metadata set! The username is")
    nananana(app.logger)

    return "success"


if __name__ == '__main__':
    with app.test_client() as c:
        c.get('/?username=batman')
