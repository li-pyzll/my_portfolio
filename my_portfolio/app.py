from flask import Flask, render_template, request

app = Flask(__name__)

# 首页路由
@app.route('/')
def index():
    return render_template('index.html')

# 作品页
@app.route('/works')
def works():
    return render_template('works.html')

# 关于我
@app.route('/about')
def about():
    return render_template('about.html')

# 留言板（GET 展示表单；POST 
# 演示收到请求，大一可后续接数据库）
@app.route('/message', methods=['GET', 'POST'])
def message():
    submitted = request.method == 'POST'
    return render_template('message.html', submitted=submitted)

if __name__ == '__main__':
    app.run(debug=True)