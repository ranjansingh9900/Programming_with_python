# day1. 1.Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

list=[]
for i in range(1500,2700):
    if (i%7)==0 and (i%5)==0:
        list.append(str(i))
    # else: continue
print(', '.join(list))


#  day1. 2.Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

def cel_to_fah(c):
    c=int(c)
    f=(9/5)*c +32
    print(f,"\u2109")
    # return f
def fah_to_cel(f):
    f=int(f)
    c=(5/9)*(f-32)
    print(c,"\u2103")
    # return c
print("You have two options: Celsius to Fahrenheit (press 1) or Fahrenheit to Celsius (press 2):")
a=input()
if a=='1':
    print("Enter Celsius")
    c=input()
    cel_to_fah(c)
elif a=='2':
    print("Enter Fahrenhit")
    f=input()
    fah_to_cel(f)
else:
    print("Invalid input: ")
