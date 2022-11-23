from data import shops
from adresses import df

print(shops)
print()

def list_of_purchases(lst: list)->dict:
    values = dict()
    for i in lst:
        for j in shops.keys():
            if j in values.keys():
                values[j] += shops[j][i]
            else:
                values[j] = shops[j][i]
    return values

print(list_of_purchases(["колбаса", "огурцы"]))

def distance(adress: str) -> dict:
    dist = dict()
    for i in shops.keys():
        dist[i] = df.loc[adress, shops[i]['адрес']]
    return dist

print(distance("ул. Авачинская, д. 20"))

def best_shop(lst: list, adress: str, v_imp = 2, d_imp = 1) -> list:
    val = list_of_purchases(lst)
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
    return [min_mag, shops[min_mag]['адрес']]

print(best_shop(["колбаса", "огурцы"], "ул. Авачинская, д. 20"))







