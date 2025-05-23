import os
import csv
from idlelib.mainmenu import default_keydefs
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def ola():
    # return '<h1>Olá, Mundo!</h1>'
    return render_template('index.html')

@app.route('/sobre-equipe')
def sobre_equipe():
    return render_template('sobre.html')

@app.route('/10anos')
def kids():
    return render_template('10anos.html')

@app.route('/iniciante')
def iniciante():
    return render_template('iniciante.html')

@app.route('/intermediario')
def intermediario():
    return render_template('intermediario.html')

@app.route('/programador')
def programador():
    return render_template('programador.html')

@app.route('/glossario')
def glossario():

    glossariodetermos = []
    with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=':')
        for t in reader:
            glossariodetermos.append(t)

    return render_template('glossario.html', glossario=glossariodetermos)

@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')

@app.route('/criar_termo', methods = ['POST'])
def criar_termo():

    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))

app.run(debug=True)
