from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello world, welcome to my MVP"
    
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return "Hello WhatsApp"

if __name__ == '__main__':
    app.run(debug=True)
