from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Dummy data for storing messages
messages = []

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages), 200

@app.route('/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    if 'message' in data:
        message = data['message']
        messages.append({'content': message})  # Store message as object with 'content' key
        return jsonify({'message': 'Message posted successfully'}), 201
    else:
        return jsonify({'error': 'Message not provided'}), 400

@app.route('/messages/clear', methods=['DELETE'])
def clear_messages():
    global messages
    messages = []  # Clear all messages
    return jsonify({'message': 'All messages cleared successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
