users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
visitors = {"Общее количество":0, "Уникальные посещения":0}
total = len(users)
unique = len(set(users))
visitors["Общее количество"] = total
visitors["Уникальные посещения"] = unique
print(visitors)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
