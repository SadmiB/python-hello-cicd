import logging
from flask import Flask, json
import logging
from datetime import datetime


logging.basicConfig(filename="app.log",format="%(asctime)8s %(levelname)-8s %(message)s")
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def hello():
    logger.info(f"{datetime.now()}, /metrics endpoint was reached")
    return "Hello Memers!"

@app.route("/status")
def status():


    logger.info(f"{datetime.now()}, /status endpoint was reached")

    response = app.response_class(
        response = json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    return response  


@app.route("/metrics")
def metrics():

    logger.info(f"{datetime.now()}, /metrics endpoint was reached")

    response = app.response_class(
            response = json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
