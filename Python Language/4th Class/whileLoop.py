'''
While Loop কী?
While Loop হলো Python-এর একটি control structure যা কোনো condition True থাকা পর্যন্ত loop execute করে।

বৈশিষ্ট্য :
Condition-based loop।
Loop কতবার চলবে তা পূর্বে জানা থাকে না।
Condition False হলে loop বন্ধ হয়ে যায়।
Careful না হলে infinite loop হতে পারে।
'''

i = 1
while i <= 5:
    print(i) #1, 2, 3, 4, 5
    i += 1