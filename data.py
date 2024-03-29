from faker import Faker
import random

my_faker = Faker("ru_RU")
Faker.seed(200)

shops = {"Шестёрочка": {"колбаса": 5, "сыр": 2, "хлеб": 3, "молоко": 7, "помидоры": 8, "огурцы": 3, "говядина": 10, "свинина": 9},
         "Диски": {"колбаса": 15, "сыр": 3, "хлеб": 3, "молоко": 7, "помидоры": 8, "огурцы": 3, "говядина": 10, "свинина": 9},
         "Компас": {"колбаса": 17, "сыр": 10, "хлеб": 3, "молоко": 7, "помидоры": 8, "огурцы": 3, "говядина": 10, "свинина": 9},
         "Повязка": {"колбаса": 17, "сыр": 10, "хлеб": 3, "молоко": 7, "помидоры": 8, "огурцы": 3, "говядина": 10, "свинина": 9},
         "Наша": {"колбаса": 17, "сыр": 10, "хлеб": 3, "молоко": 7, "помидоры": 8, "огурцы": 3, "говядина": 10, "свинина": 9},
         "Развилка": {"колбаса": 17, "сыр": 10, "хлеб": 3, "молоко": 7, "помидоры": 8, "огурцы": 3, "говядина": 10, "свинина": 9},
         "Преданный": {"колбаса": 17, "сыр": 10, "хлеб": 3, "молоко": 7, "помидоры": 8, "огурцы": 3, "говядина": 10, "свинина": 9},
         "Хорошо": {"колбаса": 17, "сыр": 10, "хлеб": 3, "молоко": 7, "помидоры": 8, "огурцы": 3, "говядина": 10, "свинина": 9}}
for i in shops.keys():
    for j in shops[i]:
        shops[i][j] = random.randint(10,100)
    str = random.randint(0,2)
    if str==0:
        shops[i]['адрес']=my_faker.bothify('ул. Авачинская, д. ##')
    elif str==1:
        shops[i]['адрес'] = my_faker.bothify('ул. Кондратьева, д. ##')
    else:
        shops[i]['адрес'] = my_faker.bothify('ул. Причудная, д. ##')

streets = ['ул. Авачинская', 'ул. Кондратьева', 'ул. Причудная']


def discount(picks):
    otvet = []
    for i in shops.keys():
        if i in picks:
            otvet.append(1)
        else:
            otvet.append(0)

    return otvet
