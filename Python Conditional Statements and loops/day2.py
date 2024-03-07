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


# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

for i in range(0,6):
    if i==3:
        continue
    else:
        print(i)



# Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

list=[0,1]
# list.append(0)
print(list)
sum=0

for i in range(0,50):
    sum=list[i]+list[i+1]
    list.append(sum)
print(*list)

print("second method")

a,b=0,1
print(a,end=",")
i=0
while i<=50:
    print(b,end=",")
    a,b=b,a+b
    i=i+1


# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

a='fizzbuzz'
b='fizz'
c='buzz'
for i in range(0,50):
    if (i%3)==0 and (i%5)==0:
        print(a)
    elif (i%3)==0:
        print(b)
    elif (i%5)==0:
        print(c)
    else:
        print(i)
