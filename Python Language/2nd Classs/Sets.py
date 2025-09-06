# Set হলো unordered collection যেখানে ডুপ্লিকেট ভ্যালু থাকে না।

# # Access Set Items
# myset = {"apple", "banana", "cherry"}

# for item in myset:
#     print(item) 


# # Add Set Items
# myset = {"apple", "banana", "cherry"}

# myset.add('orange')
# myset.update(['mango', 'graph'])
# print(myset)



# # Remove Set Items
# myset = {"apple", "banana", "cherry"}

# myset.remove('banana')
# myset.discard('apple')
# print(myset)


# # Loop Sets
# myset = {"apple", "banana", "cherry"}

# for x in myset:
#     print(x)



# Set Methods
'''union() → যোগ
intersection() → মিল
difference() → পার্থক্য'''

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))