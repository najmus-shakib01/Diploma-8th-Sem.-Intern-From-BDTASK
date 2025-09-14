#number sort student
students = [("Shakib", 85), ("Rafi", 92), ("Nadim", 78)]

sorted_student = sorted(students, key=lambda x : x[1])

print(sorted_student)