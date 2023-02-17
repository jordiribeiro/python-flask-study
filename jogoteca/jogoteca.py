from flask import Flask, render_template, request

class Jogo:
    def  __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo0= Jogo('Tetris','Arcade','Atari')
jogo1 =Jogo('Crash','ForFun','PS3')
jogo2 = Jogo('Skyrim','RPG','PS4')
lista = [jogo0,jogo1,jogo2]

app = Flask(__name__)

@app.route('/inicio')
def ola():

    return render_template('lista.html',titulo='Jogos',jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return render_template('lista.html',titulo='Jogos',jogos=lista)

app.run()