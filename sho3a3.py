"""This librar is not for the direct use"""
from typing import Any


class Sho3a3:
    def __init__(self, numbers: list[float]):
        # هذه المكتبة ليست للإستخدام المباشر
        self.sho3a3 = numbers
        self.ab3ad = (1, len(numbers))

    def __repr__(self) -> str:
        return (f"sho3a3:{self.sho3a3}")

    def __str__(self):
        return (f"sho3a3:{self.sho3a3}")

    def __len__(self):
        return len(self.sho3a3)

    def __iter__(self):
        for i in (self.sho3a3):
            yield i

    def __getitem__(self, placement):
        return self.sho3a3[placement]

    def __setitem__(self, placement, value):
        self.sho3a3[placement] = value

    # making the add of the sho3a3
    def __add__(self, other):
        """عملية طرح الشعاعين (المتجهين)"""
        if isinstance(other, Sho3a3):
            assert len(other) == len(
                self), "sho3a3s must have the same number of elements"
            jadid = []
            for i in range(len(other)):
                jadid.append(other.sho3a3[i] + self.sho3a3[i])
            return Sho3a3(jadid)
        else:
            assert isinstance(other, int) or isinstance(
                other, float), "Wrong argument type"
            return Sho3a3([element + other for element in self.sho3a3])

    def __radd__(self, other):
        assert isinstance(other, int) or isinstance(
            other, float), "Wrong argument type"
        return Sho3a3([other + element for element in self.sho3a3])

    # making the subtraction of the sho3a3
    def __sub__(self, other):
        """عملية طرح الشعاعين (المتجهين)"""
        if isinstance(other, Sho3a3):
            assert len(other) == len(
                self), "sho3a3s must have the same number of elements"
            jadid = []
            for i in range(len(other)):
                jadid.append(other.sho3a3[i] - self.sho3a3[i])
            return Sho3a3(jadid)
        else:
            assert isinstance(other, int) or isinstance(
                other, float), "Wrong argument type"
            return Sho3a3([element - other for element in self.sho3a3])

    def __rsub__(self, other):
        assert isinstance(other, int) or isinstance(
            other, float), "Wrong argument type"
        return Sho3a3([other - element for element in self.sho3a3])

    # making multiplication of the sho3a3

    def __mul__(self, other) -> float:
        if isinstance(other, Sho3a3):
            sollami = 0
            for i in range(len(self.sho3a3)):
                sollami += self.sho3a3[i] * other.sho3a3[i]
            return sollami
        else:
            assert isinstance(other, int) or isinstance(
                other, float), "Wrong argument type"
            return Sho3a3([other * element for element in self.sho3a3])

    def __rmul__(self, other):
        assert isinstance(other, int) or isinstance(
            other, float), "Wrong argument type"
        return Sho3a3([other * element for element in self.sho3a3])

    # making div of the sho3a3
    def __truediv__(self, other) -> float:
        if isinstance(other, Sho3a3):
            sollami = 0
            for i in range(len(self.sho3a3)):
                sollami += self.sho3a3[i] / other.sho3a3[i]
            return sollami
        else:
            assert isinstance(other, int) or isinstance(
                other, float), "Wrong argument type"
            return Sho3a3([other / element for element in self.sho3a3])

    def __rtruediv__(self, other):
        assert isinstance(other, int) or isinstance(
            other, float), "Wrong argument type"
        return Sho3a3([other / element for element in self.sho3a3])

    # making the power of sho3a3
    def __pow__(self, other):
        if isinstance(other, Sho3a3):
            sollami = 0
            for i in range(len(self.sho3a3)):
                sollami += self.sho3a3[i] ** other.sho3a3[i]
            return sollami
        else:
            assert isinstance(other, int) or isinstance(
                other, float), "Wrong argument type"
            return Sho3a3([element ** other for element in self.sho3a3])

    def __rpow__(self, other):
        assert isinstance(other, int) or isinstance(
            other, float), "Wrong argument type"
        return Sho3a3([other ** element for element in self.sho3a3])

    # printing the shape of the vector

    def shape(self):
        """طباعة أبعاد المتجه"""
        toul = len(self.sho3a3)
        return (1, toul)

    def sum(self)-> float:
        jam3 = 0
        for element in self.sho3a3:
            jam3 += element
        return jam3

# sho3a3_1 = Sho3a3([1, 2, 3,30, 4,20, 5.1001])

# print(sho3a3_1.sum())
# sho3a3_2 = Sho3a3([1.1, 2, 3, 4, 5])
# for num in sho3a3_1:
#     print(num)
# print(sho3a3_1)
# sho3a3_1[0] = 1000
# print(sho3a3_1 ** 2)
# print(2 ** sho3a3_1)
# print(sho3a3_1[0])
# print("Basic:",sho3a3_1)
# print("add",sho3a3_1+sho3a3_2)
# print("mul",sho3a3_1*2)
# print(2 * sho3a3_1)
# print("dot",sho3a3_1*sho3a3_2)
# print("sub",sho3a3_1-sho3a3_2)
# print(sho3a3_1-1)
# print(1-sho3a3_1)
# print("div",sho3a3_1/sho3a3_1)
