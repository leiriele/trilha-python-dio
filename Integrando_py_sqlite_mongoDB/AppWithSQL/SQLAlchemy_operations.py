from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy import select, func

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    nome_completo = Column(String)

    endereco = relationship(
        "Endereco", back_populates="usuario", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, nome_completo={self.nome_completo})"

class Endereco(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    endereco_email = Column(String(30), nullable=False)
    usuario_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="endereco")

    def __repr__(self):
        return f"Endereco(id={self.id}, endereco_email={self.endereco_email})"

def create_engine_and_tables():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    return engine

def insert_users_data(session):
    leiriele = Usuario(
        nome='Leiriele',
        nome_completo='Leiriele Correa',
        endereco=[Endereco(endereco_email='leiriele@example.com')]
    )

    maria = Usuario(
        nome='Maria',
        nome_completo='Maria Lima',
        endereco=[Endereco(endereco_email='maria@example.com')]
    )

    jorginho = Usuario(
        nome='jorginho',
        nome_completo='Jorginho do Grau',
        endereco=[Endereco(endereco_email='jorginho@example.com')]
        )

    session.add_all([leiriele, maria, jorginho])
    session.commit()

def retrieve_users_by_name(session):
    stmt = session.query(Usuario).filter(Usuario.nome.in_(["leiriele"]))
    print("Recuperando usuário com filtragem")
    for user in stmt:
        print(user)

def retrieve_addresses_by_user_id(session, user_id):
    stmt_address = session.query(Endereco).filter(Endereco.usuario_id == user_id)
    print("\n Recuperando os endereços de email!!")
    for address in stmt_address:
        print(address)

def retrieve_users_ordered_by_fullname(session):
    stmt_order = session.query(Usuario).order_by(Usuario.nome_completo.desc())
    print("\n Informações ordenadas")
    for result in stmt_order:
        print(result)

def retrieve_users_and_addresses(session):
    stmt_join = session.query(Usuario.nome_completo, Endereco.endereco_email).join(Usuario)
    print("\n Usuarios e endereços de email")
    for result in stmt_join:
        print(result)

def retrieve_users_and_addresses_with_connection(engine):
    with engine.connect() as connection:
        stmt_join = select(Usuario.nome_completo, Endereco.endereco_email).join(Usuario)
        results = connection.execute(stmt_join).fetchall()
        print("\n Testando o statement a partir de connection")
        for result in results:
            print(result)

def retrieve_user_count(session):
    stmt_count = session.query(func.count('*')).select_from(Usuario)
    print("\n Total")
    for result in stmt_count:
        print(result[0])

def main():
    engine = create_engine_and_tables()
    Session = Session(bind=engine)
    session = Session()
    insert_users_data(session)
    retrieve_users_by_name(session)
    retrieve_addresses_by_user_id(session, user_id=1)
    retrieve_users_ordered_by_fullname(session)
    retrieve_users_and_addresses(session)
    retrieve_users_and_addresses_with_connection(engine)
    retrieve_user_count(session)

    session.close()

if __name__ == "__main__":
    main()
