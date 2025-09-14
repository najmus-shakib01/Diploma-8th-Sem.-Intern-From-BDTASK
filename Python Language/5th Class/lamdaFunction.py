'''
পাইথনে ল্যাম্বডা (Lambda) ফাংশন কী?
    . ল্যাম্বডা ফাংশন হলো পাইথনের একটি ছোট অ্যানোনিমাস (নামবিহীন) ফাংশন।
    . এটা আমরা lambda কীওয়ার্ড দিয়ে লিখি।

সিনট্যাক্স :
    . lambda arguments: expression
'''

def add(a, b):
    return a + b
add_lambda = lambda a, b : a + b #দুটো কাজ একই, কিন্তু ল্যাম্বডা ফাংশন অনেক ছোট করে লেখা যায়।

print(add(5, 10)) #15
print(add_lambda(5, 10))#15

'''
ফাংশন অন্য ফাংশনের ভিতরে ব্যবহার করার জন্য (Higher-order functions) :
    . যেমন map(), filter(), sorted() ইত্যাদির সাথে বেশি ব্যবহার হয়।
'''

#number squares
numberList = [1, 2, 3, 4, 5]
squares = list(map(lambda x : x**2, numberList ))
print(squares)


#even number 
numberList = [1, 2, 3, 4, 5]
evenNumber = list(filter(lambda x : x % 2 == 0, numberList))
print(evenNumber)


#number sort student
students = [("Shakib", 85), ("Rafi", 92), ("Nadim", 78)]
sorted_student = sorted(students, key=lambda x : x[1])
print(sorted_student)