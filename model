def add_user(data):
    while True:
        name = input("Введите имя (или 'exit' для выхода): ")
        if name.lower() == 'exit':
            break
        town = input("Введите город: ")
        lastname = input("Введите фамилию: ")
        age = int(input("Введите возраст: "))
        products = {
            "name": "peperoni, mazzarella, ananass",
            "nameskuf": "peperoni, mazzarella, ananass, pivo, altushka, vodka"
        }
        if age >= 18:
            print(f"Взрослое: {products['nameskuf']}")
        elif age <= 17:
            print(f"Обычное меню: {products['name']}")
        number = int(input('Введите ваш номер: '))
        if any(user["number"] == number for user in data):
            print("Уже есть такой пользователь с этим номером.")
        else:
            data.append({"name": name, "town": town, "age": age, "lastname": lastname, "number": number})
            print("Пользователь успешно добавлен.")
            break
def search_user(data):
    search_name = input("Введите имя для поиска: ")
    found = False
    for person in data:
        if person["name"].lower() == search_name.lower():
            print(f"Данные о человеке с именем '{search_name}':")
            print(
                f"Имя: {person.get('name')}, Город: {person.get('town')}, Возраст: {person.get('age')}, Фамилия: {person.get('lastname')}, Номер: {person.get('number')}")
            found = True
            break
    if not found:
        print(f"Человек с именем '{search_name}' не найден.")
