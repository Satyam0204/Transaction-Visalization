from flask import Flask, jsonify
from requests import get
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


API_KEY = os.getenv('API_KEY')
queryid= os.getenv('QUERY_ID')


HEADER = {"x-dune-api-key" : API_KEY}

BASE_URL = "https://api.dune.com/api/v1/"

def get_query_results(queryid):
    
    url = BASE_URL + "query/" + queryid + "/results"  
    response = get(url, headers=HEADER)
    return response

def getdata():
    response = get_query_results(queryid)
    strdata = pd.DataFrame(response.json()['result']['rows'])
    transactions=strdata['Total_transactions'].to_list()
    dates=strdata['date'].to_list()
    data=dict(zip(dates,transactions))
    return data

@app.get('/')
def fetch_data():
    data =getdata()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)