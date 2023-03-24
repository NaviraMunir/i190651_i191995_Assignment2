from MLcode import getStockData
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/mylist')
def my_list():
    my_list = ['apple', 'banana', 'orange']
    return jsonify(getStockData())

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)