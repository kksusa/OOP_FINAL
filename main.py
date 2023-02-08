from manage_out_data import *
from manage_data import *
import help
db = read()
print("Это система хранения данных о внутренних номерах сотрудников предприятия.")
help.help()
while True: # Цикл проверки ввода команды
    cmd = input("Введите команду: ")
    if cmd == "add":
        add(db)
        write(db)
    elif cmd == "delete":
        delete(db)
        write(db)
    elif cmd == "list":
        list(db)
    elif cmd == "help":
        help.help()
    elif cmd == "exit":
        break
    else:
        print("Такой команды нет.\nДля вывода возможных команд введите help.")