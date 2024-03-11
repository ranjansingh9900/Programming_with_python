# Write a Python program to print the alphabet pattern 'A'.
# Expected Output:
#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *
for i in range(7):
    for j in range(5):
        if (i==0 and j==0) or (i==0 and j==4):
            print(" ",end="")
            continue
        elif (i==1 and j==1) or (i==1 and j==2) or (i==1 and j==3):
            print(" ",end="")
        elif (i==2 and j==1) or (i==2 and j==2) or (i==2 and j==3):
            print(" ",end="")
        elif (i==4 and j==1) or (i==4 and j==2) or (i==4 and j==3):
            print(" ",end="")
        elif (i==5 and j==1) or (i==5 and j==2) or (i==5 and j==3):
            print(" ",end="")
        elif (i==6 and j==1) or (i==6 and j==2) or (i==6 and j==3):
            print(" ",end="")     
        else:
            print("*",end="") 
    print()



# Write a Python program to print the alphabet pattern 'D'.
# Expected Output:
#  ****                                                                 
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  ****
    
for i in range(7):
    for j in range(5):
        if  (i==0 and j==4):
            print(" ",end="")
        elif (i==1 and j==1) or (i==1 and j==2) or (i==1 and j==3):
            print(" ",end="")
        elif (i==2 and j==1) or (i==2 and j==2) or (i==2 and j==3):
            print(" ",end="")
        elif (i==4 and j==1) or (i==4 and j==2) or (i==4 and j==3):
            print(" ",end="")
        elif (i==5 and j==1) or (i==5 and j==2) or (i==5 and j==3):
            print(" ",end="")
        elif (i==6 and j==4):
            print(" ",end="")     
        else:
            print("*",end="") 
    print()


# Write a Python program to print the alphabet pattern 'E'.
# Expected Output:
#  *****                                                                  
#  *                                                                      
#  *                                                                      
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *****



for i in range(7):
    for j in range(5):
        if (i==1 and j==1) or (i==1 and j==2) or (i==1 and j==3) or (i==1 and j==4):
            print(" ",end="")
        elif (i==2 and j==1) or (i==2 and j==2) or (i==2 and j==3) or (i==2 and j==4):
            print(" ",end="")
        elif (i==4 and j==1) or (i==4 and j==2) or (i==4 and j==3) or (i==4 and j==4):
            print(" ",end="")
        elif (i==5 and j==1) or (i==5 and j==2) or (i==5 and j==3) or (i==5 and j==4):
            print(" ",end="")   
        else:
            print("*",end="") 
    print()


# Write a Python program to print the alphabet pattern 'G'.
# Expected Output:
#   ***                                                                   
#  *   *                                                                  
#  *                                                                      
#  * ***                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 

for i in range(7):
    for j in range(5):
        if (i==0 and j==0) or (i==0 and j==4):
            print(" ",end="")
        elif (i==1 and j==1) or (i==1 and j==2) or (i==1 and j==3):
            print(" ",end="")
        elif (i==2 and j==1) or (i==2 and j==2) or (i==2 and j==3) or (i==2 and j==4):
            print(" ",end="")
        elif (i==3 and j==1):
            print(" ",end="")
        elif (i==4 and j==1) or (i==4 and j==2) or (i==4 and j==3):
            print(" ",end="")
        elif (i==5 and j==1) or (i==5 and j==2) or (i==5 and j==3):
            print(" ",end="")
        elif (i==6 and j==0) or (i==6 and j==4) :
            print(" ",end="")     
        else:
            print("*",end="") 
    print()


# Write a Python program to print the alphabet pattern 'L'.
# Expected Output:
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *****
    
for i in range(7):
    print("*",end="")
    if i==6:
        for j in range(4):
            print("*",end="")  
    print()





# Write a Python program to construct the following pattern, using a nested loop number.
# Expected Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


for i in range(10):
    for j in range(i):
        print(i,end="")
    print()

print("second approach ")
for i in range(10):
    print(str(i)*i)
