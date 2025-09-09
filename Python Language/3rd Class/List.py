# List Question

# 1. How do you create a list in Python? Write an example.
# Ans :
# Python Er Moddhe list create korte hoy thard bracket [] diye
fruits = ['apple', 'mango', 'orange', 'banana']
print(fruits) #['apple', 'mango', 'orange', 'banana']
print(type(fruits)) #<class 'list'>
print(fruits[2]) #orange 

# 2. What is the difference between append() and extend() in a list?
# Ans :
# append : Adds a single element to the end of the list.
fruits = ['apple', 'mango']
fruits.append('narikel')
print(fruits) #['apple', 'mango', 'narikel']
# extend : Adds each element of another list to the end of the list.
fruits.extend(['orange', 'banana'])
print(fruits) #['apple', 'mango', 'orange', 'banana']

# 3. Write a Python program to find the maximum and minimum values in a list.
# Ans :
numbers = [56, 78, 65, 34, 65, 89, 84]
maximum = max(numbers)
minimum = min(numbers)

print(numbers)#[56, 78, 65, 34, 65, 89, 84]
print(maximum)#89
print(minimum)#34

# 4. How do you remove duplicate values from a list?
# Ans :
value = [56, 78, 65, 34, 65, 89, 84, 84, 34]
unique_value = list(set(value))
print(unique_value)#[65, 34, 78, 84, 56, 89]

# 5. If you have fruits = ["apple", "banana", "mango"], how do you replace "banana" with "orange"?
# Ans :
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)

# 6. Given a nested list: [[1,2], [3,4], [5,6]], write code to flatten it into [1,2,3,4,5,6].
# Ans :
nested_list = [[1,2], [3,4], [5,6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)#[1, 2, 3, 4, 5, 6]

# 7. What will happen if you use a list as a default argument in a function? Why is it dangerous?
# Ans :

# Python-এ যদি আমরা কোনো mutable object (যেমন list, dict, set) কে function-এর default argument হিসাবে ব্যবহার করি, তাহলে সেই object একবারই তৈরি হয় (function define করার সময়)।
# এরপর function যতবার কল করি, প্রতিবার সেই একই object শেয়ার হয়।

# এটা dangerous, কারণ প্রোগ্রামার ভাবে প্রতিবার নতুন object তৈরি হবে, কিন্তু আসলে পুরানো object-এ ডেটা জমতে থাকে, যা unexpected behavior তৈরি করে এবং বাগ সৃষ্টি করে।

# তাই সবসময় mutable object-এর বদলে None ব্যবহার করে function-এর ভিতরে নতুন object তৈরি করা উচিত।

def add_item(item, my_list=[]):   # default argument = []
    my_list.append(item)
    return my_list

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]   
print(add_item(3))   # [1, 2, 3]
