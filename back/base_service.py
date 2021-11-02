from flask import Flask, render_template

app = Flask(__name__)


@app.route('/test')
def test():
    return "test"


@app.route('/test-template')
@app.route('/test-template/<name>')
def test_template(name=None):
    return render_template('test.html', name=name)
