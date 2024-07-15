from sqlalchemy import *
from sqlalchemy.orm import *

sqlite_database = "sqlite:///card_bank.db"
engine = create_engine(sqlite_database)


class Base(DeclarativeBase):
    pass


class PaySystem(Base):
    __tablename__ = 'pay_system'

    id = Column(Integer, primary_key=True, index=True)
    is_active_in_rf = Column(Boolean, nullable=False)
    system = Column(String, nullable=False)
    start_digits = Column(String, nullable=False)

    card = relationship('Card', back_populates='pay_system')

    def __repr__(self):
        return f'{self.id} | {self.system} | {self.is_active_in_rf} | {self.start_digits}'


class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, nullable=False)
    pay_system_id = Column(Integer, ForeignKey('pay_system.id'))

    pay_system = relationship('PaySystem', back_populates='card')
    card_bank = relationship('CardBank', back_populates='card')


class CardBank(Base):
    __tablename__ = 'card_bank'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    card_id = Column(Integer, ForeignKey('card.id'))

    card = relationship('Card', back_populates='card_bank')

Base.metadata.create_all(engine)
