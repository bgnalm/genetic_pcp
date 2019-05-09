import random

class Evolution:

    def __init__(self, order):
        pass


class Mutate:

    def __init__(self, order, number_of_pairs):
        changed = random.choice(order)
        order[changed] = random.randint(number_of_pairs)


class Breed:

    def breed(self, order1, order2):
        small = order1 if len(order1) <= len(order2) else order2
        big = order2 if len(order1) <= len(order2) else order1
        point_of_cut = random.randint(len(small))

        if random.random() < 0.5:
            return [
                small[:point_of_cut] + big[point_of_cut:],
                big[:point_of_cut] + small[point_of_cut:]
            ]






