from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "hello world"})

@app.route('/test')
def test():
    return jsonify({"message": "test"})

if __name__ == '__main__':
    app.run(debug=True)