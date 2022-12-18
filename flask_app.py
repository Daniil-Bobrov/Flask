import datetime
import os
import sqlite3

from flask import Flask, render_template, flash, redirect, session, url_for, request, abort, g

from data_base import FDataBase
import random
from forms import LoginForm

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'fdb.db')))
app.permanent_session_lifetime = datetime.timedelta(seconds=60)


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
        return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/kuku')
def hi():  # put application's code here
    return 'sdfsdf!'


@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        flash(f"Зашел пользователь под логином {form.username.data}, запомнить = {form.remember_me.data}")
        return redirect('/index')

    return render_template('login.html', title='Авторизация пользователя', form=form)


users_passwords = {'1': '12', 'user2': 'password2', 'user3': 'password3',
                   'user4': 'password4', 'user5': 'password5', 'user6': 'password6', 'user7': 'password7',
                   'user8': 'password8'}


@app.route('/login2', methods=['POST', 'GET'])
def login2():
    if 'userlogged' in session:
        return redirect(url_for('profile', username=session['userlogged']))
    elif request.method == 'POST' and request.form['username'] in users_passwords \
            and request.form['psw'] == users_passwords[request.form['username']]:
        session['userlogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userlogged']))

    return render_template('login_2var.html', title='Авторизация пользователя')


@app.route('/profile/<username>')
def profile(username):
    if 'userlogged' not in session or session['userlogged'] != username:
        abort(401)
    return f"<h1> Пользователь {username}"


@app.route('/')
@app.route('/index')
def index():
    images = {
        "cat1": {
            "text": "кот",
            "url": "https://thiscatdoesnotexist.com/"
        },
        "cat2": {
            "text": "рисунок",
            "url": "https://thisartworkdoesnotexist.com/"
        },
        "cat3": {
            "text": "лошадь",
            "url": "https://thishorsedoesnotexist.com/"
        },
        "c4": {
            "c2": "text"
        }
    }
    names = [
        "привет",
        "это самый лучший сайт",
        "как дела?",
        "не придумал("
    ]
    number = random.randint(0, 3)

    return render_template(
        "index.html",
        images=images,
        num=number,
        random=random.randint,
    )


@app.route('/petya/')
def petya():  # put application's code here
    return ''' <h2> Александр Твардовский
Василий Теркин. Сборник
Лирика
РОДНОЕ
<br>Дорог израненные спины, </br>
<br>О дальних шумных городах. </br>
    </h2> '''


@app.route('/user/<username>')
def user_profile(username):  # put application's code here
    return f"<h1>Здраствуй дорогой пользователь {username}</h1>"


@app.route('/user/<int:post_id>')
def show_post(post_id):  # put application's code here
    return f"<h1>Горячая и свежая новость № {post_id}</h1>"


@app.route('/post', methods=['POST', 'GET'])
def post():
    db = connect_db()
    db = FDataBase(db)

    if request.method == 'POST':
        if len(request.form["Заголовок статьи"]) > 3 and len(request.form["article_text"]) \
                and db.addMenu(request.form["Заголовок статьи"], "url", request.form["article_text"]):
            flash("Статья добавлена успешно", category="success")
        else:
            flash("Ошибка добавления статьи", category="error")
        # name = request.form.get("")
        # text = request.form.get('')
        # print(db.addMenu(name, 'url', text))
    print(db.getMenu())
    return render_template('post.html', title="Добавить статью")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена')


if __name__ == '__main__':
    app.run(debug=True)
