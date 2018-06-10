import os
import json
import requests
import xmltodict
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getstops')
def get_routes():

    url_site = "http://realtime.ridemcts.com"
    url_api = "/bustime/api/v1/getstops"
    url_request = url_site + url_api
    bus_routes = 'GRE'
    bus_direction = 'NORTH'
    querystring = {
    	"key": os.environ['BUSTIME_API_KEY'],
    	"rt": bus_routes,
    	"dir": bus_direction
    }
    headers = {
    	'cache-control': "no-cache"
    }

    response = requests.request("GET", url_request, headers=headers, params=querystring)
    dict_response = xmltodict.parse(response.text)

    json_response = json.dumps(dict_response['bustime-response']['stop'],
    							sort_keys=True,indent=4, separators=(',', ': '))
    return json_response

    # return json.dumps(
    #     {
    #     'temperature':str(my_temperature),
    #     'timestamp':str(my_datetime)
    #     }
    # )
