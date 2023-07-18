from flask import Flask, request, jsonify
import pyautogui
import uuid
import os

app = Flask(__name__)

API_KEY_FILE = "key.txt"

def generate_api_key():
    return str(uuid.uuid4())

def save_api_key(api_key):
    with open(API_KEY_FILE, 'w') as key_file:
        key_file.write(api_key)

def load_api_key():
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, 'r') as key_file:
            return key_file.read().strip()
    return None

def get_or_generate_api_key():
    api_key = load_api_key()
    if not api_key:
        api_key = generate_api_key()
        save_api_key(api_key)
    return api_key

@app.route('/click', methods=['POST'])
def click_mouse():
    api_key = request.headers.get('Authorization')
    expected_api_key = get_or_generate_api_key()

    if api_key != expected_api_key:
        return jsonify({'status': 'error', 'message': 'Invalid API key'}), 401

    request_data = request.get_json()
    x = request_data.get('x')
    y = request_data.get('y')

    if x is not None and y is not None:
        try:
            pyautogui.click(x=x, y=y)  # Simulate a mouse click at the specified coordinates
            return jsonify({'status': 'success', 'message': f'Mouse clicked at ({x}, {y}) successfully'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500
    else:
        # If x or y is not provided in the request, perform a regular mouse click
        try:
            pyautogui.click()
            return jsonify({'status': 'success', 'message': 'Mouse clicked successfully'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    api_key = get_or_generate_api_key()
    print(f"API key: {api_key}")
    app.run(host='0.0.0.0', port=5000)  # Change the port if required
