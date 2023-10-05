import os

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_mysqldb import MySQL

app = Flask(__name__)


mysql = MySQL(app)


@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM din_tabell")
    data = cur.fetchall()
    cur.close()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()
