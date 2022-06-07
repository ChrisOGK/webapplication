from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

pedidos = [{'id' : uuid4(),'Nome da Empresa' : 'Shift Tecnologia', 'Email' : 'shift@email.com', 'Telefone' : '17954673514', 'Quantidade de Peças' : '10', 'Tipo de Peças' : 'Gola Redonda', 'Status do Pedido' : 'Entregue'}]

@app.route('/')
def home():
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
    status = request.form['status']
    pedidos.append({'id' : uuid4(),'Nome da Empresa' : nome, 'Email' : email, 'Telefone' : telefone, 'Quantidade de Peças' : quantidade, 'Tipo de Peças' : tipo, 'Status do Pedido' : status})
    return render_template('home.html', pedidos=pedidos)

app.run(debug = True)