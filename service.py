from flask import Flask
import logging
logging.getLogger().addHandler(logging.StreamHandler())

from predict import predict_user

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'


@app.route('/<user>', methods=['GET'])
def check_in(user):
    logging.info(f"got request for {user}")
    prediction = predict_user(user)
    logging.info(f"prediction: user {user} is {prediction}")
    return prediction


if __name__ == '__main__':
    app.run()
