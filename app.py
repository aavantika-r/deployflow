import os
from flask import Flask, render_template

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/")
def home():
    return render_template("index.html", version=VERSION)


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/version")
def version():
    return {"app": "deployflow", "version": VERSION}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005) # nosec B104
