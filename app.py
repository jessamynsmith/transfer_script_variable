from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def display():
    return render_template('test.html')


@app.route('/hello', methods=['GET', 'POST'])
def background():
    var = request.form('name')
    message = "You are " + var
    print(message)
    return render_template('html_with_javascript.html', message=message)