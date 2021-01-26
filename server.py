from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
# from flask_mongoengine import MongoEngine
# from dotenv import load_dotenv

# set up
app = Flask(__name__)
CORS(app)
socket = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

######### SOCKET LISTENERS #########

@socket.on('connect')
def confirm_connect():
    print('CLIENT CONNECTED _______________________________')

@socket.on('disconnect')
def confirm_disconnect():
    print('CLIENT DISCONNECTED _____________________________')

@socket.on('hello')
def return_connect(id):
    print('hello __________________________________ hi')
    emit('hi there')



if __name__ == '__main__':
    socket.run(app)
