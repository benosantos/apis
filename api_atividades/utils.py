from models import db_session, Pessoas

def insere_pessoa():
    p = Pessoas(nome='beno', idade=23)
    print("Instância antes do save:", p)
    p.save()
    print(">> Inserido")

def consulta_pessoas():
    todos = Pessoas.query.all()
    print("Todos:", todos)

    p = Pessoas.query.filter_by(nome='Beno').first()
    if p:
        print("Beno tem", p.idade, "anos")
    else:
        print("Beno não encontrado")

def altera_pessoa():
    p = Pessoas.query.filter_by(nome='Santos').first()
    if p:
        p.idade = 21
        p.save()
        print(f">> Santos alterado para {p.idade} anos")
    else:
        print("Santos não encontrado")

def exclui_pessoa():
    p = Pessoas.query.filter_by(nome='Beno').first()
    if p:
        p.delete()
        print(">> Beno excluído")
    else:
        print("Beno não encontrado")

if __name__ == '__main__':
    # ordem de chamadas desejada:
    insere_pessoa()
    altera_pessoa()
    consulta_pessoas()
    exclui_pessoa()

    # limpa a sessão e encerra conexões
    db_session.remove()
