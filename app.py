from flask import Flask, request
from apis import api


app = Flask("Reservoir Model Results API")

api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

