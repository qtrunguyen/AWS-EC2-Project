from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

registered_users = {}

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        registered_users[username] = {
            # 'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }

        return redirect(url_for('display_info', username=username))

    return render_template('register.html')

@app.route('/display_info/<username>')
def display_info(username):
    user_info = registered_users.get(username, {})
    return render_template('display_info.html', user_info=user_info)


@app.route('/retrieve_info', methods=['GET', 'POST'])
def retrieve_info():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in registered_users and registered_users[username]['password'] == password:
            return redirect(url_for('display_info', username=username))

    return render_template('retrieve_info.html')


if __name__ == '__main__':
  app.run(debug=True)
