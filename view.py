import json

# Регистрируем пользователя
def register():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    age = input("Введите возраст: ")
    number = input("Введите номер телефона: ")
    return name, surname, age, number

def custom_pizza():
    size = input("Выберите размер (38; 40; 45): ")
    user_dopings = {}
    with open('products.json', 'r', encoding='UTF-8') as file:
        products = json.load(file)
        for product in products:
            print(product['name'])
    while True:
        user_doping = input("Что вы хотите добавить (или 'стоп'): ")
        if user_doping.lower() == 'стоп':
            return size, user_dopings
        elif user_doping in [product['name'] for product in products]:
            user_count_doping = input(f"Сколько {user_doping} вы хотите взять: ")
            user_dopings[user_doping] = user_count_doping
        else:
            print("Такого продукта нет в списке. Пожалуйста, выберите из предложенных.")

def choose_pizza():
    user_pizzas = {}
    with open('menu.json', 'r', encoding="UTF-8") as file:
        pizzas = json.load(file)
        for pizza in pizzas:
            print(pizza['pizza'])
    while True:
        user_pizza = input("Выберите пиццу ('стоп' или 'Кастомная пицца'): ")
        if user_pizza.lower() == "стоп":
            return user_pizzas
        elif user_pizza == "Кастомная пицца":
            user_pizzas[user_pizza] = '1'
            size, user_dopings = custom_pizza()
            user_pizzas[f"{user_pizza} (размер {size})"] = user_dopings
        elif user_pizza in [pizza['pizza'] for pizza in pizzas]:
            user_count = input(f"Сколько {user_pizza} вы хотите взять: ")
            user_pizzas[user_pizza] = user_count
        else:
            print("Такой пиццы нет в меню. Пожалуйста, выберите из предложенных.")

def type_of_pay(sum_of_pay):
    print(f"Итого к оплате {sum_of_pay} руб")
    pay = input("Введите тип оплаты: ")
    summ = float(input("Внесите сумму: "))
    return pay, summ

def print_check(sum_of_pay, change, products):
    for product in products:
        if isinstance(product, dict):
            print(f"{product['pizza']}: {product['price']} X {product['count']}")
    print(f'Итого: {sum_of_pay} руб')
    print(f"Сдача: {change} руб")

