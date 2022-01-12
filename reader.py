#! /usr/bin/env python3
# coding: utf-8

import csv

titles = []
lots = []


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
            print(data)
            titles.append(Action(data[0], float(data[1]), float(data[2])))

titles = sorted(titles, key=lambda x: x.renta_num, reverse=True)


for action in titles:
    print(action)
