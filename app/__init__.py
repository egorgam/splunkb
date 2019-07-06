import logging
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import configparser

logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.WARN)
log = logging.getLogger(__name__)
app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})
socketio = SocketIO(app, message_queue='redis://')
config = configparser.ConfigParser()
config.read('server.conf')
spc = config['SPLUNK']
mng = config['MONGO']

from app import routes
from app import stream
