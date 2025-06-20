from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base


engine = create_engine('sqlite:///atividades.db', echo=True, future=True)
SessionFactory = sessionmaker(bind=engine, autoflush=False, future=True)
db_session = scoped_session(SessionFactory)


Base = declarative_base()
Base.query = db_session.query_property()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id    = Column(Integer, primary_key=True)
    nome  = Column(String(40), index=True, unique=True, nullable=False)
    idade = Column(Integer, nullable=False)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return f'<Pessoa {self.nome} ({self.idade})>'

class Atividade(Base):
    __tablename__ = 'atividades'
    id        = Column(Integer, primary_key=True)
    nome      = Column(String(80), nullable=False)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'), nullable=False)
    pessoa    = relationship('Pessoa', backref='atividades')

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return f'<Atividade {self.nome} de {self.pessoa.nome}>'
    

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(80), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return f'<Usuario {self.login}>'
    
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)
