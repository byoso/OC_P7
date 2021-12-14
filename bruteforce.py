#! /usr/bin/env python3
# coding: utf-8


import itertools


from const import actions_list
from actions import Action, Lot

AMOUNT_MAX = 250
titles = []
lots = []
for item in actions_list:
    titles.append(Action(item["name"], item["price"], item["renta"]))


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
