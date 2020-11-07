import json
import os
import requests
import logging
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    logging.debug(json.dumps(req, indent=4))
    res = get_response(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def get_response(req):
    parse_request = req.get('queryResult')
    req_parameters = parse_request.get('parameters')
    city = req_parameters.get('geo-city')
    req_headers = {
        "Content-Type": "application/json"
    }
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?q=' + city + ',us&mode=xml&appid'
                                                                      '=replace-token',
        headers=req_headers)
    logging.debug(str(res.content))
    speech = "The forecast for " + city + " is : "
    return {
        "speech": speech,
        "displayText": speech,
        "source": "dialogflow-webhook"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    logging.debug('Starting app on port %d', port)
    app.run(debug=False, port=port, host='0.0.0.0')
