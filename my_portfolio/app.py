# -*- coding: utf-8 -*-
"""
个人作品集网站 - Flask 入口文件
运行方式（在项目目录 my_portfolio 下）:
    pip install -r requirements.txt
    python app.py
需要 Python 3.8+
"""

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# 用于 session 加密，生产环境请改为随机长字符串并妥善保管
app.secret_key = "dev-change-me-in-production"


@app.route("/")
def index():
    """首页"""
    return render_template("index.html")


@app.route("/projects")
def projects():
    """作品页：展示项目列表"""
    return render_template("projects.html")


@app.route("/about")
def about():
    """关于我页"""
    return render_template("about.html")


@app.route("/guestbook", methods=["GET", "POST"])
def guestbook():
    """
    留言板页
    GET: 显示留言列表与表单
    POST: 将新留言存入 session（仅作演示，刷新浏览器仍保留至 session 过期）
    """
    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        content = (request.form.get("content") or "").strip()
        if name and content:
            session["messages"] = session.get("messages", []) + [
                {"name": name, "content": content}
            ]
            session.modified = True
        return redirect(url_for("guestbook"))

    return render_template("guestbook.html", messages=session.get("messages", []))


if __name__ == "__main__":
    # debug=True 便于本地开发；上线请关闭 debug 并使用正式 WSGI 服务器
    app.run(host="127.0.0.1", port=5000, debug=True)
