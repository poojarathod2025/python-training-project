# tuple is collection of items which are indexed,ordered
# tuple are immutable
# tuple is faster than list
# syntax:tuple_name = (1,2,3)

# if there is a single element in it then put comma if we didnt put comma then its class will change.
# tup = (11,)

# methods of tuple:
# t=(20,30,40,50)
# 1.count
# c = t.count(20)-how many times 20 count
# print(c)-1 Time 
# 2.index 
# i = t.index(40)
# print(i)-2

# packing unpacking
# t = 10,"hello",True
# print(type(t))
# a,b,c,d = t-packing
# print(b)

# how to check tuple is faster than list 
# import timeit
# setup=''' 
# data_list=list(range(80000000))
# datatuple=tuple(data_list)'''
# tuple_time=timeit.timeit("for i in datatuple:pass",setup,number=1)
# list_time = timeit.timeit("for i in data_list:pass",setup=setup,number=1)
# print(list_time,"list time")
# print(tuple_time,"tuple time")
