from flask import Flask
from flask_bootstrap import Bootstrap
from controller import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecretkey'

Bootstrap(app)


@app.route('/', methods=["GET", "POST"])
def home():
    return HomePage()


if __name__ == "__main__":
    app.run()