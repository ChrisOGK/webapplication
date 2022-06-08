from flask import Flask, render_template, request, redirect
from uuid import uuid4

app = Flask(__name__)

pedidos = [{'id' : uuid4(),'Nome da Empresa' : 'Shift Tecnologia', 'Email' : 'shift@email.com', 'Telefone' : '17954673514', 'Quantidade de Pecas' : '10', 'Tipo de Pecas' : 'Gola Redonda', 'Status do Pedido' : 'Entregue'}]

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
    pedidos.append({'id' : uuid4(),'Nome da Empresa' : nome, 'Email' : email, 'Telefone' : telefone, 'Quantidade de Pecas' : quantidade, 'Tipo de Pecas' : tipo, 'Status do Pedido' : status})
    return redirect('/')

@app.route('/delete/<id>')
def apagar(id):
    numero_pedido = 0
    for pedido in pedidos:
        if id == str(pedido['id']):
            del pedidos[numero_pedido]
            return redirect('/')
        numero_pedido += 1

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
    status = request.form['status']
    pedidos[atualizar] = {'id' : id_do_pedido, 'Nome da Empresa' : nome, 'Email' : email, 'Telefone' : telefone, 'Quantidade de Pecas' : quantidade, 'Tipo de Pecas' : tipo, 'Status do Pedido' : status}
    return redirect('/')

    


app.run(debug = True)