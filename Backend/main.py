from flask import Flask, jsonify
from requests import get
import pandas as pd

app = Flask(__name__)


API_KEY = "aarHeBukLeo5XORQnylONOaWdciWlhmm"
HEADER = {"x-dune-api-key" : API_KEY}

BASE_URL = "https://api.dune.com/api/v1/"

def get_query_results(execution_id):
    
    url = BASE_URL + "query/" + execution_id + "/results"  
    response = get(url, headers=HEADER)
    return response



@app.get('/')
def fetch_data():
    data = {'data': 'Sample data'}
    response = get_query_results("2663575")
    strdata = pd.DataFrame(response.json()['result']['rows'])
    print(strdata)
    return jsonify(data)

if __name__ == '__main__':
    app.run()