from flask import Flask, render_template, request
from werkzeug.utils import redirect
from data import db_session
from data.users import User
from forms.loginform import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asjgd7823j89DB782jkD)_(mkiodaoid03hjdns873gs7a8b3*(&^#^&@bdshjd27Dghsdi3782hbr'


@app.route('/login', methods=['GET', 'POST'])
def login():
    db_session.global_init("db/blogs.db")
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form, title="а?")


@app.route("/success")
def success():
    return "Форма заполнена"


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
