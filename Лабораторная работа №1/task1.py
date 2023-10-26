numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_before_none = numbers[:4]
numbers_after_none = numbers[5:]
numbers_without_none = numbers_before_none + numbers_after_none
total = sum(numbers_without_none)
count = len(numbers)
average = total / count
numbers[4] = average
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
