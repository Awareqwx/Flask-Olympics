import flask

app = flask.Flask(__name__)

app.secret_key = "YEYAH!"

@app.route("/")
def index():
    flask.session.setdefault("visited", 0)
    flask.session["visited"] += 1
    return flask.render_template("index.html", visited = flask.session["visited"])

app.run(debug=True)