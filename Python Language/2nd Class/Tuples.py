# Tuple হলো ordered collection, কিন্তু এটি immutable (পরিবর্তন করা যায় না)।

# #Access Tuples
# colors = ("red", "green", "blue")

# print(colors[0])
# print(colors[-1])
# print(colors[1])


# # Update Tuples
# # Tuple পরিবর্তনযোগ্য না, তবে list-এ কনভার্ট করে পরিবর্তন করা যায়

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[2] = 'mango'
# x = tuple(y)
# print(x)



# # Unpack Tuples
# fruits = ("apple", "banana", "cherry")
# (a, b, c) = fruits
# print(a, b, c)


# # Loop Tuples
# fruits = ("apple", "banana", "cherry")

# for item in fruits:
#     print(item)



# Join Tuples
tuple1 = (1, 2)
tuple2 = (3, 4)

tuple3 = tuple1 + tuple2

print(tuple3)



# Tuple Methods

# count()

# index()