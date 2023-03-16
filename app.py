
from flask import Flask

app = Flask(__name__)

menu = '''
<a href="/">Pagina Inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a> 
<br>
'''

@app.route("/")
def index():
   return menu + "Meu nome é Cristian, como vai?"

@app.route("/sobre")
def sobre():
   return menu + "Aqui vai o conteúdo da página Sobre. Posso por um html depois"

@app.route("/contato")
def contato():
   return menu + "Aqui vai o conteúdo da página Contato. Entrar html depois"   