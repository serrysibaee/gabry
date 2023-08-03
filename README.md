# gabry
This is a basic implementation of matrix and vectors library to make it understandable in the context of computational matrices 

## The needed understanding of the library is like this: 

### 1. Gabry is the required library the one that should be used to use others (so it is the imported one) 
### 2. khap6 3shwaa is a randomness library from scratch (still needs a lot of work) 
### 3. sho3a3 is a vector implementation to use as a basis for another library 
### 4. masfofah is a library for matrix operations 


## Using gabry library (examples)

1. to download the gabry library just clone this repository (Inshaa Allah in the future I will make a pip install of this)

```
git clone https://github.com/serrysibaee/gabry.git 
```
Then you can use the gabry library by importing it in the code
```python
from gabry import * 
```
Then now let's make some matrix to do basic operations on it (Small note: I named the functions using Arabizi typing and I regret it now but too lazy to change it so sorry -smily face- )

##### making and printing masfofah (matrix)

```python
from gabry import * 

list1 = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

#  يصنع مصفوفة
masf = i9n3_masfofatan(list1)

print(masf,masf.shape)
``` 
##### Basic operations 
Here we can do add, sub and dot product operation for two matrices (note that in this implementation I did not add the row wise multiply maybe in the future)
```python
from gabry import * 

list1 = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]
list2 = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

# # يصنع مصفوفة
masf1 = i9n3_masfofatan(list1)
masf2 = i9n3_masfofatan(list2)


print(masf1 + masf2)
print(masf1 - masf2)
print(masf1 * masf2.man8ool()) # this is dot product 
```

#### some basic functions: 

NOTE: that sum() is similar to numpy way to do the axis summation on

```python
from gabry import * 

list1 = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

masf1 = i9n3_masfofatan(list1)


# print the shape 
print(masf1.shape)

# transpose
print(masf1.man8ool())

# summation (0 is for rows and 1 is for columns)
print(masf1.sum(axis=0))
print(masf1.sum(axis=1))
```


#### some things to add in the future inshaa Allah
1. inverse function 
2. element wise product (done see in gabry elementwise_product() function)
3. Building pip library for gabry 
4. vectors cross product and norm (NOTE: you can do them by your self as a practice for reminding you see this link [link](https://minireference.com/static/tutorials/linear_algebra_in_4_pages.pdf))
5. complete the random library khap6_3shwaa (for refrence see the book numerical recipes chapter 7 (page 340))


##### For any notes and suggested please contact me at my email " serrymrss@gmail.com " 






