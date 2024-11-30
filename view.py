import json
def register():
    name = input("Введите имя: ")
    surname = input("Ввежите фамилию: ")
    age = input("Введите возраст: ")
    number = input("Введите номер телефона: ")
    return name, surname, age, number


def custom_pizza():
    size = input("Выберите размер: 38; 40; 45: ")
    user_dopings = {}
    with open('products.json', 'r', encoding='UTF-8') as file:
        products = json.load(file)
        for product in products:
            print(product['name'])
    while True:
        user_doping = input("Что вы хотите добавить(или 'стоп'): ")
        if user_doping == 'стоп':
            return size, user_dopings
        else:
            user_count_doping = input(f"Сколько {user_doping} вы хотите взять: ")
            user_dopings[user_doping] = user_count_doping
def choose_pizza():
    user_pizzas = {}
    while True:
        user_pizza = input("Выберите пиццу('стоп' или 'Кастомная пицца'): ")
        if user_pizza == "стоп":
            return user_pizzas
        elif user_pizza == "Кастомная пицца":
            user_pizzas[user_pizza] =  '1'
        else:
            user_count = input(f"Сколько {user_pizza} вы хотите взять: ")
            user_pizzas[user_pizza] = user_count

def type_of_pay():
    pay = input("Введите тип оплаты: ")
    summ = input("Внесите сумму: ")
    return pay, summ

def print_check():
    pass
