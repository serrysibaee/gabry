# code for the new library
import typing
from masfofah import Masfofah
from khap6_3shwaa import Generator
# جداء
# العمليات الأساسية منها ضرب المصفوفات وطرحها وجمعها

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
# element wise product of both matrix and vector
def elementwise_product(masf1,masf2):
    for i in range(len(masf1)):
        masf1[i].element_wise_product(masf2[i])

def identity_masfofah(shape):
    final_masfofah = masfofah_asfar(shape,shape)
    for i in range(final_masfofah.shape[0]):
        for j in range(final_masfofah.shape[1]):
            if i == j: final_masfofah[i][j] = 1  
    return Masfofah(final_masfofah.masfofah)

def masfofah_inverse(masf):
    pass




# others 
# similar vectors by the paper 
# see 4pages linear algebra pdf 

########################################################################
gen = Generator()
def get_random():
    # return a random number (0,1)
    return gen.random_norm()
def get_random_int():
    return gen.random_int()

def random_matrix(rows,columns):
    ret = []
    for ind in range(rows):
        row = []
        for indc in range(columns):
            row.append(get_random())
        ret.append(row)
    return Masfofah(ret)

def random_matrix_int(rows,columns):
    ret = []
    for ind in range(rows):
        row = []
        for indc in range(columns):
            row.append(get_random_int())
        ret.append(row)
    return Masfofah(ret)
