from flask import Flask
from controllers import prompt_controller
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/health', methods=['GET'])
def index():
    return 'OK'

@app.route('/prompt', methods=['POST'])
def prompt():
    return prompt_controller.prompt()

if __name__ == "__main__":
    app.run(debug=True)