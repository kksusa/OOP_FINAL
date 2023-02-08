from subscriber import Subscriber

# Чтение данных из внешнего хранилища
def read():
    array = []
    temp_array = []
    with open("data.txt") as file:
        while True:
            line = file.readline()[:-1] # Исключение генерируемых при чтении символов \n для удобного вывода информации в консоль
            if not line: # Проверка на пустой файл
                break
            temp_array = line.split(" ") # Разбиение каждой записи как строки на две строки в массиве
            array.append(Subscriber(int(temp_array[0]), temp_array[1]))
    file.close()
    return array


# Запись данных во внешнее хранилище
def write(sub_array):
    with open('data.txt', 'w') as file:
        for i in range(len(sub_array)):
            file.write(f"{sub_array[i].phone_number} {sub_array[i].name}\n")
    file.close()


# Вывод списка абонентов в консоль
def list(sub_array):
    if len(sub_array) != 0: # Проверка на пустую БД
        for i in range(len(sub_array)):
            print(f"Номер: {sub_array[i].phone_number}, Абонент: {sub_array[i].name}")
    else:
        print("База данных пуста.\nДобавьте что-нибудь через add.")