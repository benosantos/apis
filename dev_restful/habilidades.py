from flask_restful import Resource

lista_habilidade = ['Python', 'Java', 'Flask', 'Django', 'PHP']

class Lista_habilidades(Resource):
    def get(self):
        return lista_habilidade
    