from flask import Flask

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return "Hello WhatsApp"

if __name__ == '__main__':
    app.run(debug=True)
