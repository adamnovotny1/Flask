from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

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
        username = request.form['username']
        password = request.form['password']
        radio = request.form['radio']
        flash("Login Succesful")
        flash("Login Unsuccesful","warning")
        return render_template('zkouska.html', username=username, password=password, radio=radio)

    return render_template('link.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'heslo':
            flash("Login Succesful")
            return render_template('login.html', login = True)
        else:
            flash("Login Unsuccesful", "warning")
            return render_template('login.html', login = False)
    return render_template('login.html')

# @app.route('/<a>/<b>')
# def multiply(a,b):
#     try:
#         multiplier = int(a) * int(b)
#         return f"Násobek je {multiplier}"
#     except ValueError:
#         return ("Neplatné číslo")

if __name__ == '__main__':
    app.run(debug=True)
