import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


from flask import Flask, jsonify

app = Flask(__name__)
web_host = "http://web:8000"
@app.route('/')
def home():
    return jsonify({"message": "hello world from call_app"})

@app.route('/test-app')
def test_app():
    response = session.get(web_host + '/test', timeout=2)
    new_message = response.json()
    return jsonify({"message": new_message})

if __name__ == '__main__':
    app.run(debug=True)