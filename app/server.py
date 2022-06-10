from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def my_home():
    return render_template('./index.html')
    # return "<p>Hello, World!</p>"


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'form submitted!'
