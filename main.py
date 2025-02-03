from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ("Hello World!<br>"
            "<a href='/kontakt'>Kontakt</a>"
            )
@app.route('/kontakt')
def contact():
    return "Kontakt"

if __name__ == '__main__':
    app.run(debug=True)