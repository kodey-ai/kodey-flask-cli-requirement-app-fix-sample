from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    Endpoint to return a simple Hello World message.
    """
    return jsonify(message="Hello, World!")

@app.route('/datetime', methods=['GET'])
def get_current_datetime():
    """
    Endpoint to return the current date and time.
    """
    now = datetime.now()
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(current_datetime=current_datetime)

@app.route('/goodbye', methods=['GET'])
def goodbye():
    """
    (Optional) Endpoint to return a Goodbye message.
    """
    return jsonify(message="Goodbye!")

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    """
    (Optional) Endpoint to greet a user by name.
    """
    return jsonify(message=f"Hello, {name}!")

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler.
    """
    return jsonify(error="Endpoint not found"), 404

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True, host="127.0.0.1", port="8888")