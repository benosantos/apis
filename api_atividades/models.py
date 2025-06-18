from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

# — Cria engine sem convert_unicode —
engine = create_engine(
    'sqlite:///atividades.db',
    echo=True,
    future=True
)

# — SessionFactory com bind (não binds) —
SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False,
    future=True
)
db_session = scoped_session(SessionFactory)

# — Base declarativa e query_property —
Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas'
    id    = Column(Integer, primary_key=True)
    nome  = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return f'<Pessoa {self.nome}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'
    id        = Column(Integer, primary_key=True)
    nome      = Column(String(80), nullable=False)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa    = relationship('Pessoas')

    def __repr__(self):
        return f'<Atividade {self.nome} de {self.pessoa.nome}>'

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
    print("Banco criado com sucesso em atividades.db")
