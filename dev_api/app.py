from flask import Flask, jsonify, request, json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Joao',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': '1',
        'nome': 'Miguel',
        'habilidades': ['Python', 'Django']
    }
]

# Devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} nao exite'
            response = {'Status': 'Error', 'Mensagem': mensagem}
        except Exception:
            mensagem = f'Erro desconhecido. Procure o administrador da API'
            response = {'Status': 'Error','Mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'menssage': 'excluido com sucesso'})


# Lista todos os Desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'Status': 'Sucesso', 'Mensagem': 'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)