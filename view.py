def register():
    name = input("Введите имя: ")
    surname = input("Ввежите фамилию: ")
    birth = input("Введите год рождения: ")
    number = input("Введите номер телефона: ")
    return name, surname, birth, number


def custom_pizza():
    size = input("Выберите размер: 38; 40; 45: ")
    user_dopings = {}
    while True:
        user_doping = input("Что вы хотите добавить(или 'стоп'): ")
        if user_doping == 'стоп':
            return user_dopings
        else:
            user_count_doping = input(f"Сколько {user_doping} вы хотите взять: ")
            user_dopings[user_doping] = user_count_doping

