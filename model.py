import json
def add_user(filename, number, name, age, surname):
    # Загружаем существующих пользователей из файла
    try:
        with open(filename, 'r', encoding="UTF-8") as users_file:
            users = json.load(users_file)
    except FileNotFoundError:
        users = []  # Если файл не найден, создаем пустой список

    # Проверяем, существует ли пользователь с таким номером
    if any(user["number"] == number for user in users):
        print("Уже есть такой пользователь с этим номером.")
        return False  # Возвращаем False, если пользователь уже существует
    else:
        # Добавляем нового пользователя
        users.append({"name": name, "age": age, "surname": surname, "number": number})
        print("Пользователь успешно добавлен.")

        # Сохраняем обновленный список пользователей в файл
        with open(filename, 'w', encoding="UTF-8") as users_file:
            json.dump(users, users_file, indent=4)
        return True  # Возвращаем True, если пользователь успешно добавлен

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def custom_pizza(user_doping,user_count_dopings):
    user_price = user_count_dopings * {user_doping['price']}
