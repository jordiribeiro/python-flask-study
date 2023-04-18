from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo0 = Jogo('Tetris', 'Arcade', 'Atari')
jogo1 = Jogo('Crash', 'ForFun', 'PS3')
jogo2 = Jogo('Skyrim', 'RPG', 'PS4')
lista = [jogo0, jogo1, jogo2]


class Login:
    def __init__(self, name, nickname, senha):
        self.name = name
        self.nickname = nickname
        self.senha = senha


usuario1 = Login("Jordi","jrf","alohomora")
usuario2 = Login("teste","teste","alohomora")
usuario3 = Login("teste1","teste1","alohomora")

usuarios = {usuario1.nickname: usuario1,usuario2.nickname:usuario2,usuario3.nickname:usuario3}

app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def comeco():
    return redirect('/inicio')


@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    else:
        return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('comeco'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + '  Logado com Sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash("Usuário não logado")
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Logout realizado com sucesso", "alert")
    return redirect(url_for('comeco'))


app.run(debug=True)
