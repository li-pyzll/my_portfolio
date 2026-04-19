# -*- coding: utf-8 -*-
"""Flask 入口：渲染作品集首页。"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """首页：返回 templates/index.html。"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
