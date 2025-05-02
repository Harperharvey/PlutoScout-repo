from flask import Flask, request, jsonify
from scout_engine import run_scout_script
from temp_account import create_temp_account
from chat_dropper import drop_chat_message
from db import log_scout_result, get_scout_logs

app = Flask(__name__)

@app.route('/')
def index():
    return "PlutoScout Backend is Running"

@app.route('/start-scout', methods=['POST'])
def start_scout():
    data = request.get_json()
    script = data.get("actions", [])
    accounts = data.get("limit", 5)
    message = data.get("message", "Hello!")

    results = run_scout_script(script, accounts, message)
    return jsonify({"result": results})

@app.route('/create-account', methods=['POST'])
def create_account():
    result = create_temp_account()
    return jsonify(result)

@app.route('/drop-message', methods=['POST'])
def drop_message():
    data = request.get_json()
    result = drop_chat_message(data)
    return jsonify(result)

@app.route('/log', methods=['POST'])
def log_result():
    data = request.get_json()
    log_scout_result(data)
    return jsonify({"status": "saved"})

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = get_scout_logs()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
