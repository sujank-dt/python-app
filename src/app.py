from flask import Flask, jsonify
from datetime import datetime
import socket
app = Flask(__name__)


@app.route('/api/v1/details')
def details():
    dt_string = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
    hostname = socket.gethostname()
    return jsonify({"hostname" :hostname , "date_time":dt_string })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({"status" : "up"}), "200"

if __name__ == '__main__':
    app.run()