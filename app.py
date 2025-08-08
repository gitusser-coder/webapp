from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

NAMEN = [

{
  'id': 1,
  'name': 'Darius',
  'Beruf': 'Softwareentwickler',
  'Alter': '24',
  'Größe': '1.82'

},

{

  'id': 2,
  'name': 'Danial',
  'Beruf': 'TikToker',
  'Alter': '22',
  'Größe': '1.71'

},

{

  'id': 3,
  'name': 'Timon',
  'Beruf': 'TikToker',
  'Alter': '22',
  'Größe': '1.70'

},

{

  'id': 4,
  'name': 'Kourosch',
  'Beruf': 'TikToker',
  'Alter': '20',
  'Größe': '1.70'

},

{

  'id': 5,
  'name': 'Nikan',
  'Beruf': 'Darmstadt',
  'Alter': '22',
  'Größe': '1.69'

}


]

@app.route('/')
def index():
  return render_template('index.html', namen=NAMEN, Geschäftsführer=Darius)


@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')


@app.route('/pdf-datei', methods=['GET', 'POST'])
def pdf():

  return render_template("pdf.html")





if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
