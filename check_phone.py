# Проверка правильности ввода номера телефона
def check_numbers(param):
    while True:
        number = input(param)
        try:
            number = int(number)
            if 99 < number < 1000: # Номер состоит из трёх цифр
                return number
            else: print("Номер введен неправильно.")
        except:
            print("Номер введен неправильно.")
