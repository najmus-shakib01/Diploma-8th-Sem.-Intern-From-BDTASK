# Tuple Question

# 1. What is a tuple? How is it different from a list?
# Ans :
# Tuple হলো Python-এর একটি ordered collection যা list-এর মতো একাধিক item রাখতে পারে।
# কিন্তু tuple immutable — মানে একবার tuple তৈরি হলে এর ভিতরের উপাদান (items) পরিবর্তন, যোগ বা মুছে ফেলা যায় না।
# Exp:
list1 = ["apple", "banana", "mango"]
tuple1 = ("apple", "banana", "mango")
print(list1)#["apple", "banana", "mango"]
print(tuple1)#("apple", "banana", "mango")

# 2. Write a tuple containing the names of 5 countries.
# Ans :
countries = ("Bangladesh", "Afganistan", "Turkey", "Egypt", "Philistine")
print(countries)#('Bangladesh', 'Afganistan', 'Turkey', 'Egypt', 'Philistine')

# 3. Can you change the value of a tuple after creating it? Why or why not?
# Ans :
# না, tuple-এর মান (value) একবার তৈরি হয়ে গেলে পরিবর্তন করা যায় না।
# কারণ tuple হলো immutable data type।

my_tuple = (10, 20, 30)
my_tuple[1] = 50    
print(my_tuple) #TypeError: 'tuple' object does not support item assignment


my_tuple = (10, 20, 30)
# Convert to list
temp_list = list(my_tuple)
temp_list[1] = 50    
my_tuple = tuple(temp_list)
print(my_tuple)   # (10, 50, 30)


# 4. How do you access the last element of a tuple?
# Ans :
countries = ("Bangladesh", "Afganistan", "Turkey", "Egypt", "Philistine")
print(countries[-1])#Philistine

# 5. Convert the tuple (10, 20, 30) into a list.
# Ans :
my_tuple = (10, 20, 30)
my_list = list(my_tuple)
print(my_list)#[10, 20, 30]

# 6. Given a tuple t = (1, [2, 3], 4), can you modify t[1][0]? Why or why not?
# Ans :
# t[1][0] modify করা যাবে।
# Tuple immutable, মানে tuple-এর ভিতরে থাকা reference (অবস্থান) change করা যায় না।

# কিন্তু tuple-এর ভিতরে যদি কোনো mutable object (যেমন list, dict, set) থাকে, তখন সেই object-এর ভেতরের মান change করা যায়।
# Example:
t = (1, [2, 3], 4)
t[1][0] = 99

print(t)#(1, [99, 3], 4)

# 7. Write a Python program that takes a list of tuples (e.g., [("a", 1), ("b", 2)]) and converts it into a dictionary.
# Ans : 
list_tuple = [("a", 1), ("b", 2), ("c", 3)]

convert_dic = dict(list_tuple)
print(list_tuple)#[('a', 1), ('b', 2), ('c', 3)]
print(convert_dic)#{'a': 1, 'b': 2, 'c': 3}


# 8. Given a nested tuple like ((1,2), (3,4), (5,6)), write a program to flatten it into a single tuple (1,2,3,4,5,6).
# Ans :
nasted_tuple = ((1,2), (3,4), (5,6))

flatten_tuple = sum(nasted_tuple, ())

print(nasted_tuple)#((1, 2), (3, 4), (5, 6))
print(flatten_tuple)#(1, 2, 3, 4, 5, 6)