import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import Crawler

#Adaptação para funcionar no meu notebook
#UPLOAD_FOLDER = '/home/kaio/Desktop/UFV/POC/Repositório/analise-usuarios/Crawlers/Flask/'
UPLOAD_FOLDER = '/home/wandella/Documentos/CrawMobi/CrawMobi-master/'
ALLOWED_EXTENSIONS = {'xls'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            redirect(url_for('upload_file', filename=filename))
            
            try:
                
                crawMobi = Crawler.crawler();
                crawMobi.menu();

                return render_template('download.html')

            except Exception as e:
                return render_template('error.html')

    return render_template('home.html')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/return-files/')
def return_files():
    try:
        #Modificação feita para funcionar na maquina da wandella
        #return send_file('/home/kaio/Desktop/UFV/POC/Repositório/analise-usuarios/Crawlers/Flask/gettingDatabase.zip',
        return send_file('/home/wandella/Documentos/CrawMobi/CrawMobi-master/gettingDatabase.zip',
                         attachment_filename='gettingDatabase.zip', as_attachment=True)
    except Exception as e:
        return str(e)


app.run(debug=True, use_reloader=True)