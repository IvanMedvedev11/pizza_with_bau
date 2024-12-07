import json


def register_user():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    age = input("Введите возраст: ")
    number = input("Введите номер телефона: ")
    return {
        "name": name,
        "surname": surname,
        "age": age,
        "number": number
    }


def load_menu():
    with open('menu.json', 'r', encoding='UTF-8') as file:
        return json.load(file)


def load_products():
    with open('products.json', 'r', encoding='UTF-8') as file:
        return json.load(file)


def calculate_price(size, dopings):
    base_price = 0
    if size == '38':
        base_price = 300
    elif size == '40':
        base_price = 350
    elif size == '45':
        base_price = 400

    products = load_products()
    for doping, count in dopings.items():
        product = next((item for item in products if item['name'] == doping), None)
        if product:
            base_price += product['price'] * int(count)

    return base_price


def create_custom_pizza():
    size = input("Выберите размер (38; 40; 45): ")
    dopings = {}
    products = load_products()

    print("Доступные добавки:")
    for product in products:
        print(product['name'])

    while True:
        user_doping = input("Что вы хотите добавить (или 'стоп'): ")
        if user_doping.lower() == 'стоп':
            break
        elif user_doping in [product['name'] for product in products]:
            user_count_doping = input(f"Сколько {user_doping} вы хотите взять: ")
            dopings[user_doping] = user_count_doping
        else:
            print("Такого продукта нет в списке. Пожалуйста, выберите из предложенных.")

    return {
        "size": size,
        "dopings": dopings
    }


def choose_pizza():
    pizzas = load_menu()
    user_pizzas = {}

    while True:
        print("Доступные пиццы:")
        for pizza in pizzas:
            print(pizza['pizza'])

        user_pizza = input("Выберите пиццу ('стоп' или 'Кастомная пицца'): ")
        if user_pizza.lower() == "стоп":
            break
        elif user_pizza == "Кастомная пицца":
            custom_pizza = create_custom_pizza()
            user_pizzas[f"Кастомная пицца (размер {custom_pizza['size']})"] = custom_pizza
        else:
            pizza = next((p for p in pizzas if p['pizza'] == user_pizza), None)
            if pizza:
                user_count = input(f"Сколько {user_pizza} вы хотите взять: ")
                user_pizzas[user_pizza] = {'count': user_count, 'price': pizza['price']}
            else:
                print("Такой пиццы нет в меню. Пожалуйста, выберите из предложенных.")

    return user_pizzas
