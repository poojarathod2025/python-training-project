# set
# set is unordered
# set is mutable
# we can store any data type
# unique elements
# duplicates/repeat are not allowed
# syntax:{}
# a={}-empty set
# print(type(a))-it will print dictionary

# methods of set-
a = {1,2,3}
b = {3,4,5}
# add-adds an element
# a.add(4)
# print(a)

# update-adds multiple elements
# a.update([5,6])
# print(a)

# remove-removes specific element
# a.remove(3)
# print(a)

# discard-removes specific element
# a.discard(3)
# print(a)

# pop -removes and returns a random element
# print(a.pop())

# copy-copy set
# c=a.copy()
# print(c)

# clear-removes all elements
# a.clear()
# print(a)

# Union-returns a new set with all elements 
# print(a.union(b))

# intersection-returns common element
# print(a.intersection(b))

# difference-
print(a.difference(b))