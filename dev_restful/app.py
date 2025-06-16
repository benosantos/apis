from flask import Flask, json, request
from flask_restful import Resource, Api
from habilidades import Lista_habilidades, Habilidades

app = Flask(__name__)
api = Api(app)

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


class Desenvolvedores(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} nao exite'
            response = {'Status': 'Error', 'Mensagem': mensagem}
        except Exception:
            mensagem = f'Erro desconhecido. Procure o administrador da API'
            response = {'Status': 'Error','Mensagem': mensagem}
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'menssage': 'excluido com sucesso'}
    


class Lista_desenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return {'Status': 'Sucesso', 'Mensagem': 'Registro inserido'}
    
    def get(self):
        return desenvolvedores
    
api.add_resource(Desenvolvedores, '/dev/<int:id>')   
api.add_resource(Lista_desenvolvedores, '/dev')
api.add_resource(Lista_habilidades, '/habilidades')

if __name__ == '__main__':
    app.run(debug=True)