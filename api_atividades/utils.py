# test_db.py
from models import init_db, db_session, Pessoa, Atividade

def main():
    init_db()
    
    p = Pessoa(nome='Santos', idade=23)
    p.save()
    print('Inserido:', p)

   
    p2 = Pessoa.query.filter_by(nome='Breno').first()
    if p2:
        p2.idade = 30
        p2.save()
        print('Alterado:', p2)

   
    print('Todas as pessoas:', Pessoa.query.all())

    
    p3 = Pessoa.query.filter_by(nome='Breno').first()
    if p3:
        p3.delete()
        print('Excluído:', p3)

    db_session.remove()

if __name__ == '__main__':
    main()
