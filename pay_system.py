from base import *


def insert_pay_systems():
    with Session(autoflush=False, bind=engine) as db:
        systems = [
            PaySystem(is_active_in_rf=True, system='Мир', start_digits='2'),
            PaySystem(is_active_in_rf=True, system='Diners Club', start_digits='30;36;38'),
            PaySystem(is_active_in_rf=False, system='JCB International', start_digits='31;35'),
            PaySystem(is_active_in_rf=False, system='American Express', start_digits='34;37'),
            PaySystem(is_active_in_rf=True, system='VISA', start_digits='4'),
            PaySystem(is_active_in_rf=False, system='Maestro', start_digits='50;56;57;58'),
            PaySystem(is_active_in_rf=True, system='MasterCard', start_digits='51;52;53;54;55'),
            PaySystem(is_active_in_rf=False, system='Discover', start_digits='60'),
            PaySystem(is_active_in_rf=True, system='China UnionPay', start_digits='62'),
            PaySystem(is_active_in_rf=True, system='Maestro', start_digits='63;67'),
            PaySystem(is_active_in_rf=True, system='УЭК (Универсальная электронная карта)', start_digits='7'),
        ]
        db.add_all(systems)
        db.commit()


def get_pay_systems():
    with Session(autoflush=False, bind=engine) as db:
        pay_systems = db.query(PaySystem).all()
        return pay_systems


# insert_pay_systems()
print(get_pay_systems())
