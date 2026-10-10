from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'message': 'Hello, Your are doing great, Human!! :) '
    })

@app.route('/api/v1/healthz')



def healthz():
    return jsonify({'status': 'up'}), 200

if __name__ == ('__main__'):

    app.run(host="0.0.0.0", port=5000, debug=True)
