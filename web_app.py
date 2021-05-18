from flask import Flask, render_template

from db_utils import get_torrent_stats

app = Flask(__name__)


@app.route('/')
def home():
    records = get_torrent_stats()
    return render_template('home.html', records=records)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)