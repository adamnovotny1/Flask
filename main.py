from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/kontakt')
def contact():
    return "Kontakt"

@app.route('/jmeno/<name>')
def hello(name):
    return f"<h1>Hello  {name}</h1>"

@app.route('/<a>/<b>')
def multiply(a,b):
    try:
        multiplier = int(a) * int(b)
        return f"Násobek je {multiplier}"
    except ValueError:
        return ("Neplatné číslo")

if __name__ == '__main__':
    app.run(debug=True)