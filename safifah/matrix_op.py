# this a optimized version of masfofah library [inspired by tsoding]
import random


class Safifah:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.masfofah = (rows * columns) * [0]
        self.total = rows * columns

    def __iter__(self):
        for i in range(len(self.masfofah)):
            yield self.masfofah

    def derefrence(self):
        return float(*self.masfofah)
    

    def lookup(self, i, j):
        return self.masfofah[i*self.columns + j]

    def change_at(self, i, j, value):
        self.masfofah[i*self.columns + j] = value

    def kolleh(self):
        return self.total

    def randomize(self):
        self.masfofah = [round(random.random(), 7)
                         for _ in range(self.total)]
        return None

    def randomize_bounded(self, min: int, max: int):
        self.masfofah = [(round(random.random(), 7)*(max-min)+min)
                         for _ in range(self.total)]



    def print_safifah(self,name) -> str:
        print(f"{name}:[")
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.lookup(i, j), end="\t")
            print()
        print("]")


def randomize_safifah(safifah):
    safifah.randomize()
    return None


def random_safifah_bound(safifah, min, max):
    safifah.randomize_bounded(3, 10)
    return None


def print_safifah(safifah,name:str=""):
    safifah.print_safifah(name)

def add(saf1, saf2):
    """first safifah is the one will be add on from the second safifah"""
    assert saf1.rows == saf2.rows
    assert saf1.columns == saf2.columns
    for i in range(saf1.total):
        saf1.masfofah[i] += saf2.masfofah[i]

    return None


def fill(saf, raqm: int):
    for i in range(saf.total):
        saf.masfofah[i] = raqm

    return None


def dot(saf_jadid, saf1, saf2):
    # s1 (a,b) s2 (b,c) j (a,c)
    assert saf1.columns == saf2.rows  # b = b
    assert saf_jadid.rows == saf1.rows  # s1.a = j.a
    assert saf_jadid.columns == saf2.columns  # s2.c = j.c

    size_saf1 = saf1.columns

    for i in range(saf_jadid.rows):
        for j in range(saf_jadid.columns):
            saf_jadid.change_at(i, j, 0)
            for k in range(size_saf1):
                now_val = saf_jadid.lookup(i, j)
                new_val = now_val + (saf1.lookup(i, k) * saf2.lookup(k, j))
                saf_jadid.change_at(i, j, new_val)

def sigmoid(z):
    from math import e 
    return (1/(1+e**-z))

def sigmoid_saf(saf):
    for i in range(saf.rows):
        for j in range(saf.columns):
            saf.change_at(i,j,sigmoid(saf.lookup(i,j))) 
