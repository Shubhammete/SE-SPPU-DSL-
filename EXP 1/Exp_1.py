# player input for Cricket
A=[]
a = int(input("Enter the number of students that play Cricket "))
print("Enter the name of",a,"students")
for i in range(0,a):
    player = input()
    if player not in A:
       A.append(player)
print("Names of Student that play Cricket")
for i in A:
    print(i)
# player input for Badminton
B=[]
a = int(input("Enter the number of students that play Badminton "))
print("Enter the name of",a,"students")
for i in range(0,a):
    player = input()
    if player not in B:
           B.append(player)
print("Names of Student that play Badminton")
for i in B:
    print(i)
    5
# player input for Football
C=[]
a = int(input("Enter the number of students that play Football "))
print("Enter the name of",a,"students")
for i in range(0,a):
    player = input()
    if player not in C:
           C.append(player)
print("Names of Student that play Football")
for i in C:
    print(i)
# Choice for operation
flag = 1
while(flag == 1):
    ch = int(input(''' 
 -----------------------------Enter your Choice -----------------------------------------
            1) List of Students who plays cricket and Badminton 
            2) List of Students who plays either cricket and badminton but not both
            3) Number of students who play neither cricket nor badminton
            4) Number of students who play cricket and football but not badminton 
            5) Exit program
----------------------------------------------------------------------------------------------------

            '''))
   # List of Students who plays cricket and Badminton 
    if ch == 1:
        lst1=[]
        for i in A:
            for j in B:
                if i == j:
                    lst1.append(i)
        print("List of Students who plays cricket and Badminton is")
        for i in lst1:
            print(i)
        y = input("Do you want to continue type 'yes': \n")
        if y == 'yes':
            flag = 1
        else:
            flag = 0
# List of Students who plays either cricket and badminton but not both 
    elif ch == 2:
       lst2=[]
       for i in A:
           if i not in B:
               if i != j:
                   lst2.append(i)
       print("List of Students who plays either cricket and badminton but not both is")
       for i in lst2:
           print(i)
       y = input("Do you want to continue type 'yes': \n")
       if y == 'yes':
            flag = 1
       else:
            flag = 0
# Number of students who play neither cricket nor badminton
    elif ch == 3:
        lst3=[]
        for i in C:
            if i not in A:
                if i not in B:
                    lst3.append(i)
        print("Number of students who play neither cricket nor badminton is",len(lst3))
        print("And their names are ")
        for i in lst3:
            print(i)
        y = input("Do you want to continue type 'yes': \n")
        if y == 'yes':
            flag = 1
        else:
            flag = 0
# Number of students who play cricket and football but not badminton
    elif ch == 4:
        lst4=[]
        for i in A:
            if i is C:
                if i not in B:
                    lst4.append(i)
        print("Number of students who play cricket and football but not badminton is",len(lst4))
        print("And their names are ")
        for i in lst4:
            print(i)
        y = input("Do you want to continue type 'yes': \n")
        if y == 'yes':
            flag = 1
        else:
            flag = 0

    elif ch == 5:
        flag = 0
        print("Thanks for using Program!!!")
    else:
        print("Enter valid Choice!!!")
        y = input("Do you want to continue type 'yes': \n")
        if y == 'yes':
            flag = 1
        else:
            flag = 0
