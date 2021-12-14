"""Module for the class Action"""


class Action:
    def __init__(self, name, price, renta):
        self.name = name
        self.price = price
        self.renta = renta

    def __str__(self):
        return (
            f"|{self.name:20} | prix: {self.price:20} | "
            f"rentabilité: {self.renta_num:20}|")

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
            f"rentabilité numéraire: {self.total_renta}"
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
