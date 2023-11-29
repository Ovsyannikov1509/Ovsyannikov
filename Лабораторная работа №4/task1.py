import json


def task() -> float:
    with open('input.json') as file:
        data = json.load(file)
        summa = sum([i['score'] * i['weight'] for i in data])
        return summa


print(f'{task():.3f}')
