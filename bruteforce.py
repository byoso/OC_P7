#! /usr/bin/env python3
# coding: utf-8

"""Actions"""

import csv


# verify the actions from the datas.csv file
def valid_data(data):
    if len(data) != 3:
        return False
    if float(data[1]) <= 0 or float(data[2]) <= 0:
        return False
    return True


def get_best(reste, n):
    counter[0] += 1
    if n == 0 or reste <= 0:
        return 0, []
    if prices[n-1] > reste:
        # the actions price is too high, let's go to the next one
        return get_best(reste, n-1)

    # 2 cases:
    # take
    renta_take, path_take = get_best(reste-prices[n-1], n-1)
    renta_take += renta[n-1]
    path_take = path_take + [actions[n-1]]

    # skip
    renta_skip, path_skip = get_best(reste, n-1)

    if max(renta_take, renta_skip) == renta_take:
        return renta_take, path_take
    else:
        return renta_skip, path_skip


if __name__ == "__main__":

    actions = []
    prices = []
    renta = []

    # load datas from the file
    with open("datas.csv", "r") as f:
        datas = csv.reader(f)
        next(datas)  # skip the header
        for data in datas:
            if valid_data(data):
                actions.append(data[0])
                price = int(float(data[1])*100)
                prices.append(price)
                rent_absolute = int(price*float(data[2]))
                renta.append(rent_absolute)

    counter = [0]

    MAX = 50000  # Max amount in cents

    renta, lot = get_best(MAX, len(actions))
    renta_result = renta/10000
    print(f"Rentabilité numeraire du lot: {renta_result}")
    print("Composition du lot:")
    for i in lot:
        print(f"{i}")
    price = 0
    for action in lot:
        index = actions.index(action)
        price += prices[index]
    price_result = price/100
    print("cout total du lot: ", price_result)
    print("iterations effectuées: ", counter[0])
