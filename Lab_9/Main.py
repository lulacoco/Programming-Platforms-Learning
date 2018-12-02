from sqlalchemy import create_engine, ForeignKey, MetaData
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy.sql import join


engine = create_engine("sqlite:///users.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

metadata = MetaData()


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    street = Column(String)
    number = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    user = relationship("User", uselist=False, back_populates="address")

    def __repr__(self):
        return "<Address(street='%s', number='%s', city='%s', state='%s', zip='%s')>" % (
            self.street, self.number, self.city, self.state, self.zip)


class Email(Base):
    __tablename__ = "email"
    id = Column(Integer, primary_key=True)
    email_1 = Column(String, nullable=True)
    email_2 = Column(String, nullable=True)
    email_3 = Column(String, nullable=True)
    user = relationship("User", back_populates="email")

    def __repr__(self):
        return "<Email(email_1='%s', email_2='%s', email_3='%s')>" % (
            self.email_1, self.email_2, self.email_3)


class Telephone(Base):
    __tablename__ = "telephone"
    id = Column(Integer, primary_key=True)
    tel_1 = Column(String, nullable=True)
    tel_2 = Column(String, nullable=True)
    tel_3 = Column(String, nullable=True)
    user = relationship("User", back_populates="telephone")

    def __repr__(self):
        return "<Telephone(tel_1='%s', tel_2='%s', tel_3='%s')>" % (
            self.tel_1, self.tel_2, self.tel_3)


#TODO lista osob powiazana z biezaca osoba
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    address_id = Column(Integer, ForeignKey('address.id'))
    email_id = Column(Integer, ForeignKey('email.id'))
    telephone_id = Column(Integer, ForeignKey('telephone.id'))

    address = relationship("Address", back_populates='user')
    email = relationship("Email", back_populates="user")
    telephone = relationship("Telephone", back_populates='user')

    def __repr__(self):
        return "<User(name='%s', surname='%s')>" % (
            self.name, self.surname)


Base.metadata.create_all(engine)


def create_user():
    name = input("Podaj imie osoby: ")
    surname = input("Podaj nazwisko osoby: ")
    street = input("Podaj ulice na ktorej mieszka osoba: ")
    number = input("Podaj numer domu osoby: ")
    city = input("Podaj miasto w ktorym mieszka osoba: ")
    state = input("Podaj wojewodztwo w ktorym mieszka osoba: ")
    zip = input("Podaj kod pocztowy osoby: ")
    email = input("Podaj email osoby: ")
    telephone = input("Podaj telefon osoby: ")

    a = Address(street=street, number=number, city=city, state=state, zip=zip)
    e = Email(email_1=email)
    t = Telephone(tel_1=telephone)
    u = User(name=name, surname=surname)

    u.address = a
    u.email = e
    u.telephone = t

    session.add(a)
    session.add(e)
    session.add(t)
    session.add(u)
    session.commit()


def find_user():
    conn = engine.connect()
    name = input("Podaj imie osoby, ktora chcesz znalezc: ")
    u = User
    a = Address
    e = Email
    t = Telephone

    ua = join(u, a, u.address_id == a.id)
    ue = join(ua, e, u.email_id == e.id)
    ut = join(ue, t, u.telephone_id == t.id)

    stmt = select([u, a, e, t]).select_from(ut).where(u.name == name)

    for row in conn.execute(stmt):
        print(row)


create_user()
find_user()
