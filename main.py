from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/kontakt')
def contact():
    return render_template('contact.html')


@app.route('/uzivatel/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.route('/odkaz', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        blog = request.form['blog']
        email = request.form['email']
        radio = request.form['radio']
        return render_template('zkouska.html', blog=blog, email=email, radio=radio)
    return render_template('link.html')

# @app.route('/<a>/<b>')
# def multiply(a,b):
#     try:
#         multiplier = int(a) * int(b)
#         return f"Násobek je {multiplier}"
#     except ValueError:
#         return ("Neplatné číslo")

if __name__ == '__main__':
    app.run(debug=True)
