from flask import Flask, request, abort
from flask_restful import Resource, Api
from models import db_session, init_db, Pessoa, Atividade

app = Flask(__name__)
api = Api(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

class PessoaResource(Resource):
    def get(self, nome):
        p = Pessoa.query.filter_by(nome=nome).first()
        if not p:
            return {'status':'error','mensagem':'Pessoa não encontrada'}, 404
        return {'id':p.id,'nome':p.nome,'idade':p.idade}

    def put(self, nome):
        p = Pessoa.query.filter_by(nome=nome).first()
        if not p:
            return {'status':'error','mensagem':'Pessoa não encontrada'}, 404
        data = request.get_json(force=True)
        if 'nome' in data: p.nome = data['nome']
        if 'idade' in data: p.idade = data['idade']
        p.save()
        return {'id':p.id,'nome':p.nome,'idade':p.idade}

    def delete(self, nome):
        p = Pessoa.query.filter_by(nome=nome).first()
        if not p:
            return {'status':'error','mensagem':'Pessoa não encontrada'}, 404
        p.delete()
        return {'status':'sucesso','mensagem':f'Pessoa {nome} excluída com sucesso'}

class ListaPessoasResource(Resource):
    def get(self):
        lista = Pessoa.query.all()
        return [{'id':x.id,'nome':x.nome,'idade':x.idade} for x in lista]

    def post(self):
        data = request.get_json(force=True)
        if not data.get('nome') or data.get('idade') is None:
            abort(400, "Informe 'nome' e 'idade'")
        p = Pessoa(nome=data['nome'], idade=data['idade'])
        p.save()
        return {'id':p.id,'nome':p.nome,'idade':p.idade}, 201

class ListaAtividadesResource(Resource):
    def get(self):
        lista = Atividade.query.all()
        return [{'id':x.id,'nome':x.nome,'pessoa':x.pessoa.nome} for x in lista]

    def post(self):
        data = request.get_json(force=True)
        if not data.get('nome') or not data.get('pessoa'):
            abort(400, "Informe 'nome' da atividade e 'pessoa'")
        p = Pessoa.query.filter_by(nome=data['pessoa']).first()
        if not p:
            return {'status':'error','mensagem':'Pessoa não encontrada'}, 404
        a = Atividade(nome=data['nome'], pessoa=p)
        a.save()
        return {'id':a.id,'nome':a.nome,'pessoa':a.pessoa.nome}, 201


api.add_resource(PessoaResource, '/pessoa/<string:nome>')
api.add_resource(ListaPessoasResource, '/pessoa')
api.add_resource(ListaAtividadesResource, '/atividades')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
