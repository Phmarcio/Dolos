from flask import Flask, render_template, redirect, url_for
from loguru import logger

logger.add("logs.log", rotation="5 MB", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/debug')
def debug():
    logger.debug('Mensagem de nível DEBUG')
    return redirect(url_for("index"))

@app.route('/info')
def info():
    logger.info('Mensagem de nível WARNING')
    return redirect(url_for("index"))

@app.route('/warn')
def warn():
    logger.warning('Mensagem de nível WARNING')
    return redirect(url_for("index"))

@app.route('/error')
def error():
    logger.error('Mensagem de nível ERRO')
    return redirect(url_for("index"))

@app.route('/critical')
def critical():
    logger.critical('Mensagem de nível CRITICAL')
    return redirect(url_for("index"))
     

if __name__ == '__main__':
    app.run(debug=True)