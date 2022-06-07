from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

pedidos = [{'id' : uuid4(),'Nome da Empresa' : 'Shift Tecnologia', 'Email de Contato' : 'shift@email.com', 'Telefone de contato' : '17954673514', 'Quantidade de Peças' : '10', 'Tipo de Peças' : 'Gola Redonda', 'Status do Pedido' : 'Entregue'}]

@app.route('/')
def home():
    return render_template('home.html', pedidos = pedidos)

app.run(debug = True)