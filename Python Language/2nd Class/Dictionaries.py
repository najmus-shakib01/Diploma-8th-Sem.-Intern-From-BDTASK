# Dictionary হলো key:value আকারে ডেটা রাখার একটি collection।

# Access Items
# student = {
#   "name": "Shakib",
#   "age": 22,
#   "dept": "CST"
# }

# print(student['name'])
# print(student.get('age'))


# # Change Items
# student = {
#   "name": "Shakib",
#   "age": 22,
#   "dept": "CST"
# }

# student['age'] = 23
# print(student)


# # Add Items
# student = {
#   "name": "Shakib",
#   "age": 22,
#   "dept": "CST"
# }

# student['roll'] = 101
# print(student)



# # Remove Items
# student = {
#   "name": "Shakib",
#   "age": 22,
#   "dept": "CST"
# }

# student.pop('age')
# del student['dept']
# print(student)



# # Loop Dictionaries

# student = {
#   "name": "Shakib",
#   "age": 22,
#   "dept": "CST"
# }

# for key, val in student.items():
#     print(key, val)



# # Copy Dictionaries

# student = {
#   "name": "Shakib",
#   "age": 22,
#   "dept": "CST"
# }

# new_student = student.copy()
# print(new_student)



# Nested Dictionaries

mydict = {
  "student1": {"name": "Shakib", "age": 22},
  "student2": {"name": "Rakib", "age": 21}
}

print(mydict['student2']['name'])



# Dictionary Methods

# keys()

# values()

# items()

# update()

# pop()