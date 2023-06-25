from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def fetch_data():
    data = {'data': 'Sample data'}
    
    return jsonify(data)

if __name__ == '__main__':
    app.run()