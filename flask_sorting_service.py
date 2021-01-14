from flask import Flask, request, jsonify, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from util import get_config, get_log, limit_content_length

app = Flask(__name__)

# get configuration
conf = get_config("configs.yaml")

MAX_CONTENT_LENGTH = conf["config"]["MAX_CONTENT_LENGTH"]

# implement rate limit
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=[
        conf["config"]["limiter"]["day"],
        conf["config"]["limiter"]["hour"],
        conf["config"]["limiter"]["second"],
    ]
)

# get logger
logobj = get_log()


@app.route('/sorting', methods=['POST'])
@limit_content_length(MAX_CONTENT_LENGTH)
def sort_list():
    """
    This route receives a list of int numbers as data, and an order for sorting
    :return: return a sorted list of data consisting of integer numbers
    """
    if not request.json:
        logobj.error(
            "Empty request.json"
        )
        abort(400)

    if not all([
        request.json.get('data'),
        request.json.get('order')
    ]):
        logobj.error(
            "KeyError, no data and no order supplied"
        )
        abort(400)
    else:
        logobj.info("request.content_length: {}".format(request.content_length))

    reverse = None
    if request.json['order'] == 'asc':
        reverse = False
    elif request.json['order'] == 'desc':
        reverse = True
    else:
        logobj.error(
            "ValueError, order is unknown"
        )
        abort(400)

    if type(request.json['data']) != list:
        logobj.error(
            "TypeError, data is not compatible, not a list"
        )
        abort(400)

    data = request.json['data']

    try:
        # timsort, Python's standard sorting algorithm since version 2.3, implemented in hand-optimized C
        data.sort(key=int, reverse=reverse)
    except ValueError as e:
        logobj.error(
            "ValueError when sorting elements from data, cannot parsing to int"
        )
        abort(400)

    return jsonify({"sorted_data": data}), 200


if __name__ == '__main__':
    app.run(debug=True)
