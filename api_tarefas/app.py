from flask import Flask, jsonify, request,json

app = Flask(__name__)

# Lista de tarefas
tarefas = [
    {
        'id': 0, 
        'responsavel': 'rafael',   
        'tarefa': 'Desenvolver método GET',  
        'status': 'concluido'
     },

    {
        'id': 1, 
        'responsavel': 'Galleani', 
        'tarefa': 'Desenvolver método POST', 
        'status': 'pendente'
    }
]

# Listar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

# Incluir nova tarefa
@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = json.loads(request.data)
    posicao = len(tarefas)
    nova_tarefa['id'] = posicao
    tarefas.append(nova_tarefa)
    return jsonify({'mensagem': 'Tarefa adicionada com sucesso!'}), 201

# Consultar uma tarefa pelo ID
@app.route('/tarefas/<int:id>', methods=['GET'])
def consultar_tarefa(id):
    try:
        response = tarefas[id]
    except IndexError:
        mensagem = f'Desenvolvedor de ID {id} nao exite'
        response = {'Status': 'Error', 'Mensagem': mensagem}
    except Exception:
        mensagem = f'Erro desconhecido. Procure o administrador da API'
        response = {'Status': 'Error','Mensagem': mensagem}
    return jsonify(response)

# Alterar o status de uma tarefa
@app.route('/tarefas/<int:id>/status', methods=['POST'])
def alterar_status(id):
    dados = request.get_json()
    novo_status = dados.get('status')
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['status'] = novo_status
            return jsonify({'mensagem': 'Status atualizado com sucesso'})
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

# Excluir uma tarefa
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    tarefas.pop(id)
    return jsonify({'mensagem': 'excluido com sucesso'})



if __name__ == '__main__':
    app.run(debug=True)