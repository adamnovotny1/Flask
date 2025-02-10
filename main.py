from flask import Flask, render_template

app = Flask(__name__)

#nastavení route pro index.html
@app.route('/')
def index():
    return render_template('index.html')

#nastavení route pro abc.html
@app.route('/abc')
def abeceda():
    return render_template('abc.html')

#nastavení route pro alfa.html
@app.route('/alfa')
def alfabeta():
    return render_template('alfa.html')

#nastavení route pro azbuka.html
@app.route('/azbuka')
def azbuka():
    return render_template('azbuka.html')

#nastavení route pro heb.html
@app.route('/heb')
def hebrejstina():
    return render_template('heb.html')

#@app.route('/uzivatel/<username>')
#def user(username):
#    return render_template('user.html', username=username)


# @app.route('/<a>/<b>')
# def multiply(a,b):
#     try:
#         multiplier = int(a) * int(b)
#         return f"Násobek je {multiplier}"
#     except ValueError:
#         return ("Neplatné číslo")

if __name__ == '__main__':
    app.run(debug=True)
