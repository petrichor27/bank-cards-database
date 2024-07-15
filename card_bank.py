from base import *


def add_card_bank(card_bank, card_id: int):
    id = None
    with Session(autoflush=False, bind=engine) as db:
        c = CardBank(card_id=card_id, firstname=card_bank.firstname, lastname=card_bank.lastname)
        db.add(c)
        db.commit()
        id = c.id
    return id


def del_card_bank(id: int):
    with Session(autoflush=False, bind=engine) as db:
        card_bank = db.query(CardBank).filter(CardBank.id == id).first()
        db.delete(card_bank)
        db.commit()


def upd_card_bank(id: int, firstname: str, lastname: str):
    with Session(autoflush=False, bind=engine) as db:
        card_bank = db.query(CardBank).filter(CardBank.id == id).first()
        card_bank.firstname = firstname
        card_bank.lastname = lastname
        db.commit()


def get_card_bank(id: int):
    with Session(autoflush=False, bind=engine) as db:
        card_bank = db.query(CardBank).filter(CardBank.id == id).first()
        return card_bank
