
import random


class gr:
    def good(self):
        return True

    def check(self, other):
        return other.good()


class br:
    def good(self):
        return False

    def check(self, other):
        return [True, False][random.randint(0, 1)]

def jig(a, b):
    return [a.check(b), b.check(a)]

def Robot_problem(Robot, verbose = False):
    def find_single(Robot):
        if len(Robot) <= 2:
            return Robot[0]
        else:
            halfpoint = len(Robot) // 2
            pairs     = zip(Robot[0:halfpoint], Robot[halfpoint:halfpoint * 2])
            kept      = [a for (a, b) in pairs if jig(a, b) == [True, True]]

            if len(Robot) % 2 == 1:
                kept.append(Robot[-1])

            return find_single(kept)

    good = find_single(Robot)
    return [Robot.index(r) for r in Robot if jig(good, r)==[True, True]]


Robot=[br(),br(),gr(),gr(),br(),br(),gr(),gr(),gr(),gr()]
#      0     1    2   3     4    5    6   7    8     9 


Robot_problem(Robot)