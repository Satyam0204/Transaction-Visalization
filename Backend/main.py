from flask import Flask, jsonify
from flask_cors import CORS
import requests
import pandas as pd
import os
from dotenv import load_dotenv
from ethereum_utils import getFirstBlockData
from datetime import datetime,timedelta


load_dotenv()
app = Flask(__name__)
CORS(app)

API_KEY = os.getenv('API_KEY')
queryid= os.getenv('QUERY_ID')


HEADER = {"x-dune-api-key" : API_KEY}

BASE_URL = "https://api.dune.com/api/v1/"

def get_query_results(queryid):
    
    url = BASE_URL + "query/" + queryid + "/results"  
    response = requests.get(url, headers=HEADER)
    return response

def getdata():
    response = get_query_results(queryid)
    strdata = pd.DataFrame(response.json()['result']['rows'])
    transactions=strdata['Total_transactions'].to_list()
    dates=strdata['date'].to_list()
    data=dict(zip(dates,transactions))
    return data

@app.get('/get-arbritrum-transactions')
def fetch_data():
    try:
        data =getdata()

        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.get('/ethereum-data/<date>')
def getlatestblockdata(date):
    desired_date=datetime.strptime(date,'%Y-%m-%d')
    try:
        first_block_number=getFirstBlockData(desired_date)
        last_block_number=getFirstBlockData(desired_date+timedelta(1))-1

        res={"first_block_number":first_block_number,"last_block_number":last_block_number}
        return jsonify(res)

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)