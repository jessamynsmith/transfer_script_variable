from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def display():
    return render_template('html_with_javascript.html')


@app.route('/hello', methods=['POST'])
def post():
    # Get the parsed contents of the form data
    json = request.get_json()
    print(json)
    return jsonify(json)