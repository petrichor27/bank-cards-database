from base import *


def add_card(card):
    id = None
    with Session(autoflush=False, bind=engine) as db:
        c = Card(number=card.card_number, pay_system_id=card.pay_system[0])
        db.add(c)
        db.commit()
        id = c.id
    return id


def del_card(id: int):
    with Session(autoflush=False, bind=engine) as db:
        card = db.query(Card).filter(Card.id == id).first()
        db.delete(card)
        db.commit()


def upd_card(id: int, card_number: str, pay_system_id: int):
    with Session(autoflush=False, bind=engine) as db:
        card = db.query(Card).filter(Card.id == id).first()
        card.number = card_number
        card.pay_system_id = pay_system_id
        db.commit()


def get_card(id: int):
    with Session(autoflush=False, bind=engine) as db:
        card = db.query(Card).filter(Card.id == id).first()
        return card
