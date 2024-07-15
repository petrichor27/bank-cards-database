from card import add_card
from card_bank import add_card_bank
from pay_system import get_pay_systems


class CardBankMain:
    def __init__(self, firstname, lastname, card):
        self.firstname = firstname
        self.lastname = lastname
        self.card = card
        self.card_id = None
        self.id = None

    def __str__(self):
        return f'{self.firstname} {self.lastname} ' + str(self.card)

    def add_to_db(self):
        card_id = add_card(self.card)
        id = add_card_bank(self, card_id)
        self.card_id = card_id
        self.id = id


class CardMain:
    def __init__(self, card_num):
        self.card_number = self.validator(card_num)
        self.pay_system = self.get_pay_system(card_num)

    def __str__(self):
        return f'{self.card_number} {self.pay_system[1]} {"Работает" if self.pay_system[2] else "Не работает"}'

    def validator(self, card):
        if self.luhn(card):
            return card
        else:
            raise ValueError('Неверный номер карты')

    @staticmethod
    def luhn(card):
        sum = 0
        card = ''.join(card.split())
        card_nums = list(map(int, card))
        card_nums.reverse()

        for index, num in enumerate(card_nums, start=1):
            if index % 2 == 0:
                temp = num * 2
                sum += ((temp % 10) + 1) if temp > 9 else temp
            else:
                sum += num
        return sum % 10 == 0

    @staticmethod
    def get_pay_system(card):
        pay_systems = get_pay_systems()
        for s in pay_systems:
            digits = s.start_digits.split(';')
            if card[:1] in digits or card[:2] in digits:
                return s.id, s.system, s.is_active_in_rf
        raise ValueError('Нет подходящей платежной системы')


firstname = input("Имя --> ")
lastname = input("Фамилия --> ")
card_num = input("Номер карты --> ")

card1 = CardMain(card_num)
card_bank1 = CardBankMain(firstname, lastname, card1)
print(card_bank1)
card_bank1.add_to_db()
