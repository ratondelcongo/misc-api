from flask import Flask
from flask import jsonify
from flask import request
import utils


def create_app():
    app = Flask(__name__)
    return app


app = create_app()
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def hello_world():
    return "<p>xd!</p>"


@app.route('/api/v1/horoscope_by_sign', methods=['GET'])
def horoscope_by_sign():
    args = request.args
    sign = args.get("sign")
    result = utils.get_horoscope(sign)
    response = jsonify({'result': result})
    return response


@app.route('/api/v1/horoscope_all', methods=['GET'])
def horoscope_all():
    result = utils.getHoroscopeAll()
    print(result)
    response = jsonify(result)
    return response


@app.route('/api/v1/clasificatorias_qatar', methods=['GET'])
def getClasi():
    result = utils.getTablaClasificatoriasQatar()
    print(result)
    response = jsonify(result)
    return response


if __name__ == '__main__':
    app.run(debug=True)
