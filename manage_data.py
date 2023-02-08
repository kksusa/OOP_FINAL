from check_phone import check_numbers
from subscriber import Subscriber


# Добавление экземпляра абонента
def add(sub_array):
    phone = check_numbers("Введите номер телефона: ")
    for i in range(len(sub_array)):
        if phone == sub_array[i].phone_number: # Проверка на наличие записи в БД
            print("Такой номер уже есть в базе данных.")
            return sub_array
        else:
            continue
    name = input("Введите абонента: ")
    sub_array.append(Subscriber(phone, name))
    print("Номер добавлен.")
    return sub_array


# Удаление экземпляра абонента
def delete(sub_array):
    if len(sub_array) != 0: # Проверка на пустую БД
        check = False # Флаг для проверки вхождения записи в БД
        phone = check_numbers("Введите номер телефона: ")
        for i in range(len(sub_array)):
            if phone == sub_array[i].phone_number:
                del sub_array[i]
                print(f"Номер {phone} удален.")
                check = True
                break
        if not check:
            print("Такого номера нет.")
    else: print("База данных пуста.\nДобавьте что-нибудь через add.")
    return sub_array

