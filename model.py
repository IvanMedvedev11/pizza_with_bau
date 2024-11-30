
def add_user(data,number,name,age,surname):
    if any(user["number"] == number for user in data):
        print("Уже есть такой пользователь с этим номером.")
    else:
        data.append({"name": name,"age": age, "surname": surname, "number": number})
        print("Пользователь успешно добавлен.")
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
