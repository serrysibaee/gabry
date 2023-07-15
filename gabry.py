# code for the new library
import typing
from masfofah import Masfofah

# جداء
# العمليات الأساسية منها ضرب المصفوفات وطرحها وجمعها


# 
# make matrix of zeros
def masfofah_asfar(rows: int, columns: int):
    new_masfofah = []
    for row in range(rows):
        new_masfofah.append(columns*[0])
    
    return Masfofah(new_masfofah)

# make matrix of ones 
def masfofah_wahidat(rows: int, columns: int):
    new_masfofah = []
    for row in range(rows):
        new_masfofah.append(columns*[1])
    
    return Masfofah(new_masfofah)


# create a matrix 
def i9n3_masfofatan(qaimah:list[float]):
    return Masfofah(qaimah)

# create a vector i9n3 -> make 
def i9n3_sho3a3an(qaimah:list[float]):
    return Masfofah(qaimah)
# dot product of both matrix and vector
# others 
# similar vectors by the paper 
# see 4pages linear algebra pdf 


# print(masfofah_asfar(3,1))
# print(masfofah_wahidat(3,1))
