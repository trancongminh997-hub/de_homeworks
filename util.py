from functools import wraps
import logging
import yaml
from flask import request, abort


def get_config(config_file):
    with open(config_file, 'r') as f:
        conf = yaml.load(f, Loader=yaml.SafeLoader)
    return conf


def get_log():
    logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
    return logging.getLogger()


def limit_content_length(max_length):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cl = request.content_length
            if cl is not None and cl > max_length:
                abort(413)
            return f(*args, **kwargs)
        return wrapper
    return decorator
