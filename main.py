from flask import Flask, render_template

app = Flask(__name__)

#nastavení route pro index.html
@app.route('/')
def index():
    return render_template('index.html')

#nastavení route pro abc.html
@app.route('/abc')
def abc():
    return render_template('abc.html')

#nastavení route pro alfa.html
@app.route('/alfa')
def alfa():
    return render_template('alfa.html')

#nastavení route pro azbuka.html
@app.route('/azb')
def azb():
    return render_template('azb.html')

#nastavení route pro heb.html
@app.route('/heb')
def heb():
    return render_template('heb.html')

@app.route('/<cokoliv>')
def jine_abecedy(cokoliv):
    return render_template('jine_abecedy.html', cokoliv=cokoliv)


# @app.route('/<a>/<b>')
# def multiply(a,b):
#     try:
#         multiplier = int(a) * int(b)
#         return f"Násobek je {multiplier}"
#     except ValueError:
#         return ("Neplatné číslo")

if __name__ == '__main__':
    app.run(debug=True)
