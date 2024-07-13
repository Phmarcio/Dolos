from flask import Flask, render_template, redirect, url_for
import logging
from logging import info, debug, warning, error, critical

app = Flask(__name__)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/debug')
def debug():
    logging.debug('MENSAGEM DEBUG')
    return redirect(url_for("index"))

@app.route('/info')
def info():
    logging.info('MENSAGEM INFO')
    return redirect(url_for("index"))

@app.route('/warn')
def warn():
    logging.warning('MENSAGEM WARNING')
    return redirect(url_for("index"))

@app.route('/error')
def error():
    logging.error('MENSAGEM ERROR')
    return redirect(url_for("index"))

@app.route('/critical')
def critical():
    logging.critical('MENSAGEM CRITICAL')
    return redirect(url_for("index"))
     

if __name__ == '__main__':
    app.run(debug=True)