def find_common_participants(str1, str2, i=','):
    a = str1.split(i)
    b = str2.split(i)
    set1 = set(a)
    set2 = set(b)
    participants = set1.intersection(set2)
    result = sorted(list(participants))
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)

#Эта версия кода считается корректной, но она выдает неверный ответ. Правильная версия кода предствлена ниже:
'''
def find_common_participants(str1, str2, i='|'):
    a = str1.split(i)
    b = str2.split(i)
    set1 = set(a)
    set2 = set(b)
    participants = set1.intersection(set2)
    result = sorted(list(participants))
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)
'''