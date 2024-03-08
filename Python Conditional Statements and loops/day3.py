# Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]


array=[]
i=int(input("Enter row: "))
j=int(input("Enter columns: "))
for row in range(i):
    list=[]
    for col in range(j):
        # x=input("Enter : ")
        list.append(row*col)
    array.append(list)
    print(list)

print(array)


# Write a Python program that accepts a sequence of lines (blank line to terminate) as 
# input and prints the lines as output (all characters in lower case).

def main():
    lines = []  # Initialize a list to store input lines
    
    # Accept input lines until a blank line is encountered
    while True:
        line = input("Enter a line (blank line to terminate): ")
        if not line.strip():  # Check if the line is blank
            break
        lines.append(line)  # Add non-blank line to the list
    
    # Convert each input line to lowercase and print it
    print("\nOutput (in lowercase):")
    for line in lines:
        print(line.lower())

if __name__ == "__main__":
    main()




# Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as 
# its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010

print("convert binary to decimal")
num=int(input("enput: "))
sum=0
i=0
while num>0:
    a=num%10
    sum=sum+(2**i)*a
    num=num//10
    # print(sum)
    i+=1
print(sum)

print("Convert into decimal to binary")
li=[]
while sum>0:
    a=sum%2
    # print(a)
    sum=sum//2
    li.append(a)
li.reverse()
print(*li)




# Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

st=input("Enput: ")
di=0
st1=0
for i in st:
    if i.isdigit():
        di+=1
    else: st1+=1

print("Sum Of digit: ",di)
print("Sum of char: ",st1)


