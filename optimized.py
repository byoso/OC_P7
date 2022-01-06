#! /usr/bin/env python3
# coding: utf-8

"""Optimized version, based on a greedy algorithme"""


import csv


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


def valid_data(data):
    if len(data) != 3:
        return False
    if float(data[1]) <= 0 or float(data[2]) <= 0:
        return False
    return True


with open("datas.csv", "r") as f:
    datas = csv.reader(f)
    next(datas)  # skip the header
    for data in datas:
        if valid_data(data):
            titles.append(Action(data[0], float(data[1]), float(data[2])))

titles = sorted(titles, key=lambda x: x.renta_num, reverse=True)

amount = 0
bag = []
while amount < AMOUNT_MAX:
    if titles:
        title = titles.pop(0)
        if amount + title.price < AMOUNT_MAX:
            amount += title.price
            bag.append(title)
    else:
        break


print(f"\nMeilleur lot pour un investissement max de {AMOUNT_MAX}:")
renta = 0
for action in bag:
    print(action)
    renta += action.renta_num
print(f"Prix du lot: {amount}")
print(f"rentabilité numéraire: {renta:.2f}")
