from model import calculate_price
def display_user_info(user):
    print("\nИнформация о пользователе:")
    print(f"Имя: {user['name']}")
    print(f"Фамилия: {user['surname']}")
    print(f"Возраст: {user['age']}")
    print(f"Номер телефона: {user['number']}")


def display_pizza_selection(user_pizzas):
    print("\nВыбранные пиццы:")
    total_price = 0
    for pizza, details in user_pizzas.items():
        if 'size' in details:  # Кастомная пицца
            price = calculate_price(details['size'], details['dopings'])
            total_price += price
            print(f"{pizza}: {price} руб (размер {details['size']})")
        else:  # Обычная пицца
            price = int(details['count']) * details['price']
            total_price += price
            print(f"{pizza}: {price} руб (количество: {details['count']})")

    print(f"\nИтого к оплате: {total_price} руб")
    return total_price
            print(f"{product['pizza']}: {product['price']} X {product['count']}")
    print(f'Итого: {sum_of_pay} руб')
    print(f"Сдача: {change} руб")
