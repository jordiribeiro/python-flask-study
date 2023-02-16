from flask import Flask, render_template

class Jogo:
    def  __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1= Jogo('Tetris','Arcade','Atari')
    jogo2 =Jogo('Crash','ForFun','PS3')
    jogo3 = Jogo('Skyrim','RPG','PS4')
    lista = [jogo1,jogo2,jogo3]
    return render_template('lista.html',titulo='Jogos',jogos=lista)

app.run()