from flask import Flask, render_template, request, redirect
from uuid import uuid4
import csv

app = Flask(__name__)

pedidos = []
with open('Pedidos.csv', 'rt') as entrada:
  leitor = csv.DictReader(entrada)
  for pedido in leitor:
      pedidos.append(dict(pedido))

pedidos = sorted(pedidos, key= lambda pedidos: pedidos['Nome da Empresa'])


def salvar_csv():
    with open('Pedidos.csv', 'wt') as saida:
        escritor = csv.DictWriter(saida, ['id', 'Nome da Empresa', 'Email', 'Telefone', 'Quantidade de Pecas', 'Tipo de Pecas'])
        escritor.writeheader()
        escritor.writerows(pedidos)

@app.route('/')
def home():
    salvar_csv()
    return render_template('home.html', pedidos = pedidos)

@app.route('/new_order')
def novo_pedido():
    return render_template('new_order.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    quantidade = request.form['quantidade']
    tipo = request.form['tipo']
    pedidos.append({'id' : uuid4(),'Nome da Empresa' : nome, 'Email' : email, 'Telefone' : telefone, 'Quantidade de Pecas' : quantidade, 'Tipo de Pecas' : tipo})
    return redirect('/')

@app.route('/delete/<id>')
def apagar(id):
    for pedido in pedidos:
        if id == str(pedido['id']):
            del pedidos[pedidos.index(pedido)]
            return redirect('/')

@app.route('/update/<id>')
def atualizar(id):
    for pedido in pedidos:
        if id == str(pedido['id']):
            return render_template('atualizar.html', pedido=pedido)

@app.route('/update/atualizar/<id>', methods=['POST'])
def salvar_atualização(id):
    for pedido in pedidos:
        if id == str(pedido['id']):
            atualizar = pedidos.index(pedido)
            id_do_pedido = pedido['id']
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    quantidade = request.form['quantidade']
    tipo = request.form['tipo']
    pedidos[atualizar] = {'id' : id_do_pedido, 'Nome da Empresa' : nome, 'Email' : email, 'Telefone' : telefone, 'Quantidade de Pecas' : quantidade, 'Tipo de Pecas' : tipo}
    return redirect('/')

@app.route('/ordenar')
def ordenar():
    global pedidos
    pedidos = sorted(pedidos, key= lambda pedidos: pedidos['Nome da Empresa'])
    return redirect('/')

    


app.run(debug = True)