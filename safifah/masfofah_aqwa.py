# this a optimized version of masfofah library [inspired by tsoding]
import random


class Safifah:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.masfofah = (rows * columns) * [0]
        self.majmoo3 = rows * columns

    def lookup(self, i, j):
        return self.masfofah[i*self.columns + j]

    def change_at(self, i, j, value):
        self.masfofah[i*self.columns + j] = value

    def kolleh(self):
        return self.majmoo3

    def lkhbetha(self):
        self.masfofah = [round(random.random(), 7)
                         for _ in range(self.majmoo3)]
        return None

    def lkhbeth_b7d(self, aql: int, a3la: int):
        self.masfofah = [(round(random.random(), 7)*(a3la-aql)+aql)
                         for _ in range(self.majmoo3)]

    def lkhbetha(self):
        self.masfofah = [round(random.random(), 7)
                         for _ in range(self.majmoo3)]

    def print_safifah(self) -> str:
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.lookup(i, j), end=" ")
            print()


def lkhbet_safifah(safifah):
    safifah.lkhbetha()
    return None


def lkhbet_safifah_b7d(safifah, aql, a3la):
    safifah.lkhbeth_b7d(3, 10)
    return None


def jam3(saf1, saf2):
    """first safifah is the one will be add on from the second safifah"""
    assert saf1.rows == saf2.rows
    assert saf1.columns == saf2.columns
    for i in range(saf1.majmoo3):
        saf1.masfofah[i] += saf2.masfofah[i]

    return None


def t3bba(saf, raqm: int):
    for i in range(saf.majmoo3):
        saf.masfofah[i] = raqm

    return None


def jodaa(saf_jadid, saf1, saf2):
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
