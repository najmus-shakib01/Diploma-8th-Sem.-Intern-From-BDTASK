# Set Question

# 1. What is a set in Python? How is it different from a list?
# Ans :
# Set হলো Python-এর একটি collection data type, যা unordered, unindexed, এবং unique elements রাখে।
# Ordered (index থাকে), Allowed (repeat হতে পারে), Mutable (change করা যায়), Access by index (my_list[0]), তৈরি হয় [] দিয়ে

# List example
my_list = [1, 2, 2, 3]
print(my_list)   # [1, 2, 2, 3] 

# Set example
my_set = {1, 2, 2, 3}
print(my_set)#{1, 2, 3}


# 2. Write a Python program to find the union of two sets.
# Ans :
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1.union(set2)

print(union)#{1, 2, 3, 4, 5}

# 3. What happens if you add duplicate elements to a set?
# Ans :
# Python-এর set হলো unordered collection of unique elements।
# তাই যদি set-এ duplicate element add করলে, সেটা ignore হয়ে যাবে।
set1 = {1, 2, 3, 5, 6, 7, 3, 2, 4, 7, 4}

add_duplicate = set(set1)
print(add_duplicate)#{1, 2, 3, 4, 5, 6, 7}

# 4. How do you check if an element exists in a set?
# Ans :
set1 = {1, 2, 3, 5, 6, 7, 3, 2, 4, 7, 4}

print(3 in set1)#True
print(99 in set1)#False

# 5. Write a program to find the intersection of {1,2,3,4} and {3,4,5,6}.
# Ans :
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1.intersection(set2)
print(intersection)#{3, 4}