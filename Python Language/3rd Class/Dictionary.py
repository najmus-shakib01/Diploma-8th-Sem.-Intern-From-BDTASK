# Dictionary

# 1. What is a dictionary in Python?
# Ans : 
# পাইথনে ডিকশনারি হল key : value পেয়ার এবং এটি ডিক্লেয়ার করতে হয় {} কারলি ব্রেসেস দিয়ে।
# Exp :
dictionary = {
    'name' : 'shakib',
    'age' : 22
}

print(dictionary)#{'name': 'shakib', 'age': 22}

# 2. Create a dictionary of 3 students with their names as keys and ages as values.
# Ans : 
student = {
    "Rahim": 20,
    "Karim": 22,
    "Hasan": 19
}
print(student)#{'Rahim': 20, 'Karim': 22, 'Hasan': 19}

# 3. How do you access the value of a dictionary using a key?
# Ans :
dictionary = {
    'name' : 'shakib',
    'age' : 22
}

print(dictionary['name'])#shakib
print(dictionary['age'])#22

# 4. Write a program to update the value of a dictionary key.
# Ans :
dictionary = {
    'name' : 'shakib',
    'age' : 22
}

dictionary['name'] = 'Rakib'

print(dictionary)

# 5. What will happen if you try to access a key that does not exist in a dictionary?
# Ans :
# যদি কোনো key না থাকে আর dict[key] দিয়ে access তরি → তখন KeyError হবে।
students = {
    "Rahim": 20, 
    "Karim": 22
}
print(students['hasan'])#KeyError: 'hasan

# 6. What is the difference between dict.get(key) and dict[key]? Show with an example.
# Ans :
students = {
    "Rahim": 20, 
    "Karim": 22
}

print(students['Rahim'])#20
print(students.get('Karim'))#22
print(students.get('Hasan', 0))#0

# 7. Explain how nested dictionaries work with an example of storing student data (name, subjects, marks).
# Ans :
students = {
    'Rahim' :{
        'Subjects' : {
            'Math' : 85,
            'Englis' : 78,
            'Science' : 92
        }
    },
    'Karim' : {
        'Subjects':{
            'Bangla' : 75,
            'Agricalture' : 88,
            'Networking' : 80
        }
    }
}

print(students['Rahim']['Subjects'])#{'Math': 85, 'Englis': 78, 'Science': 92}
print(students['Karim']['Subjects'])#{'Bangla': 75, 'Agricalture': 88, 'Networking': 80}