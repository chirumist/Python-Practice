"""
Lambda function and map function
map function just like loop
filter function for filter with condition
"""
# arr = ["3","4","6"]
# num = list(map(int,arr))
# print(num[0] + 1)
# print(num)
# square = list(map(lambda a: a*a,num))
# print(square)


numbers = [3, 4, 5, 6, 7, 8, 9, 11, 12, 13]

# funcs = [lambda x: x,lambda x: x * x, lambda y: y * y * y]
# print("Filter with lambda function usage")
# print(list(filter(lambda x: x>5,numbers)))
# print("Map with lambda function usage")
# for item in numbers:
#     print(list(map(lambda x:x(item),funcs)))

# import functools
# functools.reduce()
from functools import reduce
print("Reduce function")
numbers1 = [1,2,3,4]
print(reduce(lambda x,y:x+y,numbers1))
# or
num = 0
for i in numbers1:
    num = num + i

print(num)