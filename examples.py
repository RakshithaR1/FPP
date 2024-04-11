 

strings = ["apple","mango","banana"]

mapping = map(len,strings)

mapped = list(mapping)
print(f"Length of the strings {strings} are {mapped}")

from functools import reduce


total_length = reduce(lambda x,y : x+y,mapped)
print(f"The total length of the strings is {total_length}")

#Lambda helps in creating an anyonomous function
#reduce operates on the entire list and iterates every element
#map operates on each and every element of the list and returns the output of the function performed on each element 
x=10
assert x==10
#assert is usually used for debbugging.it is basically used to check the values in variables, it shows an assertion error
#if the value to be checked does not match the variable's value
#only expressions can be passed to the lambda function since "assert" is a keyword and not an 
# expression it cannot be passed to lambda

