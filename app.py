from flask import Flask
from flask import render_template, request, flash
from forms import *

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
def hello():
    form = Registro()
    if request.method == 'POST':
        if form.validate() == 'False':
            flash('All fields are required')
            render_template('index.html', form = form)
        else:
            name, last_name, email = form.name.data, form.last_name.data, form.email.data
            submission_successful = True
            return render_template('registro.html', name = name, last_name = last_name, email = email)
    elif request.method == 'GET':
        return render_template('index.html', form = form)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = '8080')
