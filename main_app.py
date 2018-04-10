from flask import Flask, render_template
from store import Image

app = Flask(__name__)


@app.route("/")
def index():
    images = Image.all()
    return render_template('index.html', images=images)


if __name__ == '__main__':
    app.run()
