# List হলো একটি ordered collection, যেখানে একাধিক ডেটা রাখা যায়। এটি পরিবর্তনযোগ্য (mutable)।

# # Access List Items
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[-1])



# # Change List Items
# fruits = ["apple", "banana", "cherry"]
# fruits[1] = 'mango'
# print(fruits)



# # Add List Items
# fruits = ["apple", "banana", "cherry"]
# fruits.append('orange')
# fruits.insert(1, 'mango')
# print(fruits)



# # Remove List Items
# fruits = ["apple", "banana", "cherry"]
# fruits.remove('apple')
# fruits.pop(1)
# del fruits[0]
# print(fruits)   



# # Loop Lists
# fruits = ["apple", "banana", "cherry"]

# for item in fruits:
#     print(item)



# # List Comprehension
# numbers = [x for x in range(10) if x % 2 == 0]
# print(numbers)



# # Sort List
# num = [3, 1, 5, 2, 5]
# num.sort()
# print(num)



# # Copy List
# fruits = ["apple", "banana", "cherry"]
# new_list = fruits.copy()
# print(new_list)


# Join Lists
list1 = [1, 3]
list2 = [4, 5]

list3 = list1 + list2

print(list3)


# List Methods

# append()

# insert()

# remove()

# pop()

# sort()

# copy()

# extend()