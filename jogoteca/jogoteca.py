from flask import Flask, render_template, request, redirect, session, flash

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
app.secret_key='alura'
@app.route('/')
def comeco():
    return redirect('/inicio')

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Jogos',jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    else:
        return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado']=request.form['usuario']
        flash(session['usuario_logado'] + ' Usuário Logado com Sucesso!')
        return redirect('/')
    else:
        flash("Usuário não logado")
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Logout realizado com sucesso","alert")
    return redirect('/')

app.run(debug=True)