import time
import datetime
import pandas as pd
from flask import Flask, Response, json, request, jsonify
from sklearn.externals import joblib
from stock_prediction import StockPrice

FILENAME = 'finalized_model.sav'
app = Flask(__name__)


def input_date(str):
    temp_date = time.mktime(datetime.datetime.strptime(str, "%d/%m/%Y").timetuple())
    return pd.DataFrame({'Date': [temp_date]})


def load_predict(df):
    loaded_model = joblib.load(FILENAME)
    return loaded_model.predict(df)


@app.route('/')
def api_root():
    return 'Welcome to stock prediction services'


# input: date as string
# returns: predicted stock price
@app.route('/stockprice', methods=['POST'])
def api_stockprice():
    if request.is_json:
        content = request.get_json()
        df = input_date(content['date'])
        predictedvalue = load_predict(df)
        data = {
            'price': predictedvalue.item(0),
        }
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')

    return resp


# input: list of dates
# returns: list of predicted stock prices
@app.route('/stockprices', methods=['POST'])
def api_stockprices():
    if request.headers['Content-Type'] == 'application/json' and request.is_json:
        stockpricelist = []

        for item in request.json['stock']:
            df = input_date(item['date'])
            predictedvalue = load_predict(df)
            price = StockPrice(predictedvalue.item(0))
            stockpricelist.append(price)
            data = {
                'stock': [e.toJSON() for e in stockpricelist]
            }
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp
    else:
        return "Unsupported Request"


if __name__ == '__main__':
    app.run()
