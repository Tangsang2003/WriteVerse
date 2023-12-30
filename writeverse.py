from flask import Flask, render_template, url_for
app = Flask(__name__)

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
        'content' : 'Second posts content',
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


if __name__ == '__main__':
    app.run(debug=True)
