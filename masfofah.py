from sho3a3 import Sho3a3


class Masfofah:
    def __init__(self, sho3a3s: list[float]):
        self.masfofah = [Sho3a3(row) for row in sho3a3s]
        self.shaper = self.shape()

    def __repr__(self) -> str:
        return "masfofah:\n"+"\n".join(str(mas.sho3a3) for mas in self.masfofah)+"\n"

    def shape(self):
        rows = len(self.masfofah)
        columns = len(self.masfofah[0])
        return (rows, columns)

    def __len__(self) -> int:
        return len(self.masfofah)

    def __add__(self, other):
        assert self.shape[0] == other.shape[0] and self.shape[
            1] == other.shape[1], "not the same size"
        adder = []
        for index in range(len(self.masfofah)):
            adder.append(self.masfofah[index] + other.masfofah[index])

        return Masfofah(adder)

    def __mul__(self, other):
        assert self.shape[1] == other.shape[0]
        # this is a dot product multiplication of masfofah and other
        multiplier = []
        for row in self.masfofah:
            row_with_column = []
            for column in other.extract_columns():
                row_with_column.append(row * column)
            multiplier.append(row_with_column)

        return Masfofah(multiplier)

    def __sub__(self, other):
        assert self.shape[0] == other.shape[0] and self.shape[
            1] == other.shape[1], "not the same size"
        subber = []
        for index in range(len(self.masfofah)):
            subber.append(self.masfofah[index] - other.masfofah[index])
        
        return Masfofah(subber)

    def __getitem__(self, place):
        return self.masfofah[place]

    def extract_columns(self):
        new_masfofah = []
        for i in range(len(self.masfofah[0].sho3a3)):
            new_column = []
            for j in range(len(self.masfofah)):
                new_column.append(self.masfofah[j].sho3a3[i])
            new_masfofah.append(new_column)
        return Masfofah(new_masfofah)

    # sum of the columns and rows about the axis
    def sum(self, axis):
        """ترجع مجموع العناصر حسب الإتجاه فالصفر يحسب نزولا على الصفوف والواحد أفقيا على الأعمدة"""
        returned_sum = []
        if axis == 0:
            over_rows_sum = []
            for column in self.extract_columns():
                over_rows_sum.append(column.sum())
            returned_sum = over_rows_sum
        if axis == 1:
            over_columns_sum = []
            for row in self.masfofah:
                over_columns_sum.append(row.sum())
            returned_sum = over_columns_sum

        return Masfofah([returned_sum])

    # return transpose of matrix 
    def man8ool(self):
        return self.extract_columns()

    
    # adding and removing columns and rows
    def add(self,other, axis=0):
        # make sure that the size of the new input is correct
        if axis == 0:
            for i in range(len(self.masfofah)):
                self.masfofah[i].sho3a3.extend(other.masfofah[i].sho3a3)
        if axis == 1: 
            self.masfofah.extend(other.masfofah)
        pass

    def remove(self,other,axis=0):
        pass 
    
    # we could take rid of this function
    def print_columns(self):
        for i in range(len(self.masfofah[0].sho3a3)):
            for j in range(len(self.masfofah)):
                print(self.masfofah[j].sho3a3[i], end=" ")
            print('\n')

    


# masfofah_1 = Masfofah([[1, 2, 3],
#                        [4, 5, 6],
#                        [1, 2, 3]])
# masfofah_2 = Masfofah([[1, 2, 3],
#                        [4, 5, 6],
#                        [1, 2, 3]])

# masfofah_1.add(masfofah_2 , axis=0)
# print(masfofah_1.shape())


# masfofah_1 = Masfofah([[1, 2, 3],
#                        [4, 5, 6],
#                        [1, 2, 3]])
# masfofah_2 = Masfofah([[1, 2, 3],
#                        [4, 5, 6],
#                        [1, 2, 3]])
# masfofah_1.add(masfofah_2 , axis=1)
# print(masfofah_1.shape())

# print(masfofah_1.sum(axis=0))
# print(masfofah_1.sum(axis=0).man8ool().shape)
# print(masfofah_1)
# masfofah_1_T = masfofah_1.man8ool()
# print(masfofah_1_T)
# masfofah_2 = Masfofah([[1, 2, 3],
#                      [4, 5, 6],
#                      [1, 2, 3]])
# masfofah.print_columns()

# print(masfofah[0:2])
# print(masfofah)
# print(masfofah_1)
# print("shape of the masfofah is: ",masfofah_1.shape())

# masfofah_3 = masfofah_1 * masfofah_2

# print(masfofah_1)
# print(masfofah_2.extract_columns())
# print(masfofah_3)

# masfofah_5 = Masfofah([[1,2,3,4,5]])
# masfofah_6 = Masfofah([[1],[2],[3],[4],[5]])
# print(masfofah_5,masfofah_6)
# print(masfofah_5.shape())
# print(masfofah_6.shape())

# print(masfofah_5*masfofah_6)
