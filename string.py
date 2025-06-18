# strings can be written in single,double,triple quote.
# single and double quote are same.
# triple quote is used for paragraphs.
# eg.my name is "suraj"
# print("my name is 'suraj'")

# slicing
# it includes start:end:steps
# str1 = "hello"
# print(str1[::-1])-reverse String 
# print(str1[0:3])
# print(str1[::2])
# print(str1.upper())

# strip remove space from beginning and End 
# my_str = "india is my country."
# print(len(my_str))
# print(len(my_str.strip()))

# concatenate
# first_name = "suraj"
# last_name ="deore"
# print(first_name + "\n" + last_name)
# a=10,b=20
# print(a,b)

# \'-
# print()
# print('it\s me')
# print('it\s me')

# \r- removes beginning Part 
# print('it\rs me')

# \t -moves 4 steps ahead
# str1='it me !\t'-8 index position of \t+count remaining characters first 8 jhala
# then substract from next 8 i.e.8-7
# print(len(str1.expandtabs()))
# print(len(str1))
# len function doesnt calculate \t spaces assume as 1 space only

# \b-1 space back hoil n letter delete hoil
# print('i\bts me')

# methods of String 
# s = "hello world"
# print(s.strip())-removes whitespace
# print(s.upper())-HELLO WORLD
# print(s.lower())-hello world
# print(s.replace("world","python"))-hello Python 
# print(s.split())-'hello','world'
# print(s.find("lo"))-3
