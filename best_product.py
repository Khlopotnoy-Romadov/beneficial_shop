from data import shops
from adresses import df
import random, copy

print(shops)
print()

def list_of_purchases(lst: list, shops: dict)->dict:
    values = dict()
    for i in lst:
        for j in shops.keys():
            if j in values.keys():
                values[j] += shops[j][i]
            else:
                values[j] = shops[j][i]
    return values

print(list_of_purchases(["колбаса", "огурцы"], shops))

def distance(adress: str) -> dict:
    dist = dict()
    for i in shops.keys():
        dist[i] = df.loc[adress, shops[i]['адрес']]
    return dist

print(distance("ул. Авачинская, д. 20"))

def discount_card()->dict:
    disc = dict()
    for i in shops.keys():
        disc[i] = random.randint(3, 9)
    return disc

print(discount_card())

def best_shop(lst: list, adress: str, v_imp = 2, d_imp = 1, cards = [0]*len(shops)) -> list:
    shops1 = dict()
    for i in shops.keys():
        shops1[i] = copy.deepcopy(shops[i])
    disc = discount_card()
    for i in range(len(cards)):
        if cards[i]!=0:
            print(shops1[list(shops1.keys())[i]])
            for j in shops1[list(shops1.keys())[i]].keys():
                if j!='адрес':
                    shops1[list(shops1.keys())[i]][j]=round(shops1[list(shops1.keys())[i]][j]-shops1[list(shops1.keys())[i]][j]*disc[list(shops1.keys())[i]]*0.01)
    val = list_of_purchases(lst, shops1)
    dis = distance(adress)
    res = dict()
    for i in val.keys():
        res[i] = val[i]*v_imp + dis[i]*d_imp//2
    min = 10000000
    min_mag = ""
    for i in res.keys():
        if res[i] < min:
            min = res[i]
            min_mag = i
    return [min_mag, shops[min_mag]['адрес'], val, dis]

print(best_shop(["колбаса", "огурцы"], "ул. Авачинская, д. 20", cards = [1,1,0,0,0,0,0,0]))







