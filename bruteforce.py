#! /usr/bin/env python3
# coding: utf-8

"""This is the brute force solution for the client"""


import csv
import itertools

# Change this value to match the client's maximum amount to invest
AMOUNT_MAX = 500


class Action:
    def __init__(self, name, price, renta):
        self.name = name
        self.price = price
        self.renta = renta

    def __str__(self):
        return (
            f"|{self.name:20} | prix: {self.price:20} | "
            f"rentabilité: {self.renta_num:20.2f}|")

    def __repr__(self):
        return f"<Action {self.name}>"

    @property
    def renta_num(self):
        return self.price*self.renta/100


class Lot:
    count = 0

    def __init__(self, *args):
        Lot.count += 1
        self.name = f"lot n°{Lot.count:10} "
        self.actions = []
        for arg in args:
            self.actions.append(arg)

    def __str__(self):
        return (
            f"{self.name:20} | prix: {self.total_price:10} | "
            f"rentabilité numéraire: {self.total_renta:10.2f}"
        )

    def __repr__(self):
        return f"<Lot {self.name}>"

    def show_actions(self):
        for action in self.actions:
            print(action)

    @property
    def total_price(self):
        total = 0
        for action in self.actions:
            total += action.price
        return total

    @property
    def total_renta(self):
        rentability = 0
        for action in self.actions:
            rentability += action.price*action.renta/100
        return rentability


titles = []
lots = []

with open("datas.csv", "r") as f:
    datas = csv.reader(f)
    for data in datas:
        titles.append(Action(data[0], int(data[1]), int(data[2])))

# for item in actions_list:
#     titles.append(Action(item["name"], item["price"], item["renta"]))


def get_possibilities(titles):
    number_of_actions = len(titles)
    all_possibilities = []
    for i in range(1, (number_of_actions+1)):
        possibilities = list(itertools.combinations(titles, i))
        all_possibilities.extend((possibilities))
    return(all_possibilities)


def get_best(results):
    result = ""
    best_renta = 0
    best_lot = None
    for line in results:
        lot = Lot(*line)
        if lot.total_price <= AMOUNT_MAX:
            if lot.total_renta > best_renta:
                best_renta = lot.total_renta
                best_lot = lot
            lots.append(lot)
            result += f"\n\n*{lot}"
            for action in lot.actions:
                result += f"\n{action}"
    return best_lot


def print_lot(lot):
    result = (
        f"La meilleure rentabilité possible pour un "
        f"investissement maximum de {AMOUNT_MAX} Euros s'obtient avec "
        f"le lot suivant :\n")
    result += f"\n{lot}"
    for action in lot.actions:
        result += f"\n{action}"
    with open("best_lot.txt", "w") as f:
        f.write(result)
    print(result)


def print_unwanted_lots(lots):
    detail = ""
    for lot in lots:
        detail += f"\n\n{lot}"
        print(lot)
        for action in lot.actions:
            detail += f"\n{action}"
    with open("all_lots.txt", "w") as f:
        f.write(detail)


all_results = get_possibilities(titles)
best_lot = get_best(all_results)
print_unwanted_lots(lots)
print_lot(best_lot)
