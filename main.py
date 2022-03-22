from flask import Flask, render_template, request
from werkzeug.utils import redirect
from data import db_session
from data.users import User
from forms.loginform import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asjgd7823j89DB782jkD)_(mkiodaoid03hjdns873gs7a8b3*(&^#^&@bdshjd27Dghsdi3782hbr'


@app.route('/reg', methods=['GET', 'POST'])
def login():
    db_session.global_init("db/blogs.db")
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('reg.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('reg.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        if request.method == 'POST':
            user = User()
            user.name = request.form["name"]
            user.surname = request.form["surname"]
            user.address = request.form["address"]
            user.email = request.form["email"]
            user.hashed_password = request.form["password"]
            user.position = request.form["position"]
            user.age = request.form["age"]
            user.speciality = request.form["speciality"]
            db_sess = db_session.create_session()
            db_sess.add(user)
            db_sess.commit()
        return redirect('/success')
    return render_template('reg.html', form=form, title="а?")


@app.route("/success")
def success():
    return "Форма заполнена"


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
