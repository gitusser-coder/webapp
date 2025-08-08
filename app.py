from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')


@app.route('/pdf-datei', methods=['GET', 'POST'])
def pdf():

  return render_template("pdf.html")


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
