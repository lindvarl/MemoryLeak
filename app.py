from flask import Flask, request
from apis import api
import logging

app = Flask("Reservoir Model Results API")

api.init_app(app)
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

