def add_user(data,number,name,age,surname):
    if any(user["number"] == number for user in data):
        print("Уже есть такой пользователь с этим номером.")
    else:
        data.append({"name": name,"age": age, "surname": surname, "number": number})
        print("Пользователь успешно добавлен.")
def search_user(data):
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
