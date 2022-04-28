
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play')
def display():
    return render_template('index.html', num=3, color="cyan")


@app.route('/play/<int:num>')
def repeat(num):
    return render_template('index.html', num=num, color="cyan")


@app.route('/play/<int:num>/<string:color>')
def choose_color(num, color):
    return render_template('index.html', num=num,  color=color)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
