'''
লুপ কেন ব্যবহার করা হয়?
একই কাজ বারবার করতে হলে কোড পুনরায় লিখতে না গিয়ে loop ব্যবহার করা হয়।
Data structure-এর সব elements process করতে সহজ হয়।
Program-এর efficiency বাড়ে।
'''

'''
For Loop হলো Python-এর একটি control structure যা একটি sequence (list, tuple, string, range, etc.) এর সব element-এ iterate করার জন্য ব্যবহার করা হয়।

বৈশিষ্ট্য :
Sequence অনুযায়ী iteration হয়।
Iteration সংখ্যা fixed বা নির্দিষ্ট।
Loop body প্রতিটি element-এর জন্য একবার execute হয়।
'''

fruits = ['apple', 'banana', 'cherry']
for i in fruits:
    print(i) #apple, banana, cherry


for i in range(1, 6):
    print(i)#1, 2, 3, 4, 5