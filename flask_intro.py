from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test')
def test_txt():
    return 'test text shows here'

@app.route('/html_test')
def html_test():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()