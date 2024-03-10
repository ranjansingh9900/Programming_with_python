# Write a Python program to find numbers between 100 and 400 (both included) 
# where each digit of a number is an even number. The numbers obtained should be printed in a 
# comma-separated sequence.
def check(i):
    while i!=0:
        a=i%10
        print(a)
        i=i//10
        if a%2==0:
            continue
        else:
            return False
    return True
li=[]
for i in range(100,401):
    x=check(i)
    if x==True:
        li.append(i)
    
print(li)

print("second approach")

li1=[]
for i in range(100,401):
    i=str(i)
    if (int(i[0])%2==0) and (int(i[1])%2==0) and (int(i[2])%2==0):
        li1.append(i)

print(li1)



#  Write a Python program to check the validity of passwords input by users.
# Validation :
# •	At least 1 letter between [a-z] and 1 letter between [A-Z].
# •	At least 1 number between [0-9].
# •	At least 1 character from [$#@].
# •	Minimum length 6 characters.
# •	Maximum length 16 characters.

import re
print("""At least 1 letter between [a-z] and 1 letter between [A-Z]
 	At least 1 number between [0-9]
 	At least 1 character from [$#@]
 	Minimum length 6 characters
 	Maximum length 16 characters""")
pas=input("Enter password: ")
flag=0
if not re.search('[A-Z]',pas):
    flag=1
if not re.search('[a-z]',pas):
    flag=1
if not re.search('[0-9]',pas):
    flag=1
if not re.search('[!@#$&?]',pas):
    flag=1
if not 6<len(pas):
    flag=1
if not 16>=len(pas):
    flag=1

if flag==1:
    print("Invail passwaord: ")
else:
    print("correct: ")
