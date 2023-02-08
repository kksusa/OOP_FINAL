# Класс абонента
class Subscriber:
    name = None
    phone_number = None

    def __init__(self, phone_number, name):
        self.name = name
        self.phone_number = phone_number
