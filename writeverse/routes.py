from writeverse.models import User, Post
from writeverse import app
from flask import render_template, url_for, flash, redirect
from writeverse.forms import RegistrationForm, LoginForm

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
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created For {form.username.data}!', 'success')
        return redirect(url_for("home"))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful! Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)