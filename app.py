from flask import Flask
import os
from config import load_configurations, configure_logging

app = Flask(__name__)

# Load configurations and logging settings
load_configurations(app)
configure_logging()

@app.route('/', methods=['GET'])
def home():
    # Test: Logging environment variables
    logging.info(app.config['ACESS_TOKEN'])
    logging.info(app.config["APP_ID"])
    logging.info(app.config["APP_SECRET"])
    logging.info(app.config["RECIPIENT_WAID"])
    logging.info(app.config["VERSION"])
    logging.info(app.config["PHONE_NUMBER_ID"])
    logging.info(app.config["VERIFY_TOKEN"])
    return "Hello world, welcome to my MVP"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return "Hello WhatsApp"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
