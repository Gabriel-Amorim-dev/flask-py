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

@app.route('/basico')
def basico():
    return render_template('basico.html')
@app.route('/selecao')
def selecao():
    return render_template('selecao.html')
@app.route('/vetmat')
def vetmat():
    return render_template('vetomatriz.html')
@app.route('/repeticao')
def repeticao():
    return render_template('repeticao.html')
@app.route('/funepro')
def funcepro():
    return render_template('funceproc.html')
@app.route('/traexc')
def traexc():
    return render_template('trateexce.html')
@app.route('/bibliotecas')
def bibliotecas():
    return render_template('bibliotecas.html')
@app.route('/datanalise')
def datanalise():
    return render_template('dataanalise.html')

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

@app.route('/excluir_termo')
def excluir_termo():
    return render_template('excluir_termo.html')

@app.route('/alterar_termo')
def alterar_termo():
    return render_template('alterar_termo.html')

@app.route('/criar_termo', methods = ['POST'])
def criar_termo():

    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'r+', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))

@app.route('/remover_termo', methods = ['POST'])
def remover_termo():

    termos = request.form['termo']
    termos_restantes = []

    with open('bd_glossario.csv', 'r+', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for i in reader:
            if i[0] != termos:
                termos_restantes.append(i)

    with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(termos_restantes)

    return redirect(url_for('glossario'))

@app.route('/trocar_termo', methods = ['POST'])
def trocar_termo():
    termo = request.form['termo']
    novo_termo = request.form['novo_termo']
    nova_definicao = request.form['nova_definicao']
    termos = []


    with open('bd_glossario.csv', 'r+', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for i in reader:
            if i[0] == termo:
                termos.append([novo_termo, nova_definicao])
            else:
                termos.append(i)

    with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(termos)

    return redirect(url_for('glossario'))

app.run(debug=True)
