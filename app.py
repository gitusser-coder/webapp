from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

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
  'Beruf': 'Autohersteller',
  'Alter': '22',
  'Größe': '1.69'

}


]

@app.route('/')
def index():
  return render_template('index.html', namen=NAMEN, Geschäftsführer='Darius')


@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')


@app.route('/pdf-datei', methods=['GET', 'POST'])
def pdf():
    return render_template("pdf.html")

@app.route('/fill_pdf', methods=['POST'])
def fill_pdf():
    try:
        # Formulardaten abrufen
        vorname = request.form.get('vorname', '')
        nachname = request.form.get('nachname', '')
        geburtsdatum = request.form.get('geburtsdatum', '')
        geburtsort = request.form.get('geburtsort', '')
        
        # Erstelle echte PDF mit reportlab
        pdf_buffer = BytesIO()
        pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)
        
        # PDF-Inhalt erstellen
        pdf_canvas.setTitle("Ausgefülltes Formular")
        pdf_canvas.setFont("Helvetica-Bold", 16)
        pdf_canvas.drawString(100, 750, "PDF FORMULAR - AUSGEFÜLLT")
        
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(100, 700, f"Vorname: {vorname}")
        pdf_canvas.drawString(100, 680, f"Nachname: {nachname}")
        pdf_canvas.drawString(100, 660, f"Geburtsdatum: {geburtsdatum}")
        pdf_canvas.drawString(100, 640, f"Geburtsort: {geburtsort}")
        
        pdf_canvas.setFont("Helvetica-Oblique", 10)
        pdf_canvas.drawString(100, 600, "Erstellt mit der Flask PDF-App")
        
        pdf_canvas.save()
        pdf_buffer.seek(0)
        
        return send_file(
            pdf_buffer,
            as_attachment=False,
            download_name=f'{nachname}_{vorname}_formular.pdf',
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/vorschau')
def vorschau():
    return render_template('vorschau.html')





if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5001, debug=True)
