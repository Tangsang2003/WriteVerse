from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '154ba97b464eaa4546579d0d0c7648d1'

posts = [
    {
        'author': 'Tangsang Chongbang',
        'title': 'Blog Post 1',
        'content': 'First posts content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'John Cena',
        'title': 'Blog Post 2',
        'content': 'Second posts content',
        'date_posted': 'April 23, 2020'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
