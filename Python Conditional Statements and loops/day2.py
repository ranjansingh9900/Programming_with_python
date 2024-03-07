# Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# *

for i in range(0,10):
    if i<=5:
        for j in range(i):
            print("* ",end='')
        print()
    else:
        for j in range(10-i):
            print("* ",end='')
        print()

print("second approach")

for i in range(1,6):
    print('* '*i)
for i in range(4,0,-1):
    print('* '*i)



#  Write a Python program that accepts a word from the user and reverses it.

s=str(input("Enter string:"))
# print(len(s))
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
print()
print("second approach")

reversed_s=s[::-1]

print(reversed_s)



#  Write a Python program to guess a number between 1 and 9.
#  Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess
#  is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random
rand_no=random.randint(1,9)
print(rand_no)
print("you have two option: press 1 for plying , 2 for Not playing")
x=int(input())
if x==1:
    guess=int(input("Enter a number between 1 and 9: "))
    while guess!=rand_no:
        print("guess Wrong: try again")
        guess=int(input("Enter a number between 1 and 9: "))
    print("Well guessed!")
else:
    print("thank you")
