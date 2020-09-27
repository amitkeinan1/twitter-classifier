from flask import Flask, request, jsonify

from predict import predict_user

app = Flask("tweeter-classifier")


@app.route('/')
def hello():
    return 'Hello!'


@app.route('/<user>', methods=['GET'])
def check_in(user):
    return predict_user(user)


if __name__ == '__main__':
    app.run(host='localhost', port=2612)
