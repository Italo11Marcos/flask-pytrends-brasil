from flask import Flask, render_template
from index import google_trends

app = Flask(__name__)


@app.route('/')
def index():
    trends = google_trends()
    return render_template('index.html', trends=trends)


if __name__ == "__main__":
    app.run(debug=True)