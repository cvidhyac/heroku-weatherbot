import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    res = get_response(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def get_response(req):
    parse_request = req.get('queryResult')
    req_parameters = parse_request.get('parameters')
    city = req_parameters.get('geo-city')
    date = req_parameters.get('date')
    req_headers = {
        "Content-Type": "application/json"
    }
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?q=' + city + ',us&mode=xml&appid'
                                                                      '=e973b4ce27b0763ac378205ebc955c60',
        headers=req_headers)
    print(str(res.content))
    speech = "The forecast for " + city + "for " + date + ""
    return {
        "speech": speech,
        "displayText": speech,
        "source": "dialogflow-webhook"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print('Starting app on port %d', port)
    app.run(debug=False, port=port, host='0.0.0.0')
