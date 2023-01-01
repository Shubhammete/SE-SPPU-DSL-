a = int(input("Enter the number of students "))
marks = []
print("Enter the marks of",a,"students (Enter -1 for absent student) ")
for i in range(0,a):
    num = int(input())
    marks.append(num)
print('''-------------------------------------------------------''')
print("The marks of ",a,"students")
realnum = list(filter(lambda x : x > 0, marks))
for i in realnum:
    print(i)
flag = 1
while(flag == 1):
    ch = int(input('''
                    1) Average of class
                    2) Highest and Lowest score
                    3) No of students who were absents 
                    4) Display marks with highest frequency
                    5) Exit program
                 '''))
    if ch == 1:
        sum = 0
        realnum = list(filter(lambda x : x > 0, marks))
        for i in realnum:
            sum =sum + i
        avg = sum/len(realnum)
        print("The average of class is",avg)
        c=input("Do you want to continue: ")
        if c == 'yes':
            flag = 1
        else:
            flag = 0
            print("Thanks for using program!!!")

    
    elif ch == 2 :
        realnum = list(filter(lambda x : x > 0, marks))
        realnum.sort()
        print("The highest scorer of class is",realnum[0])
        print("The lowest scorer of class is",realnum[-1])
        c=input("Do you want to continue: ")
        if c == 'yes':
            flag = 1
        else:
            flag = 0
            print("Thanks for using program!!!")

    elif ch == 3:
        count = 0
        for i in marks:
         if i == -1:
            count = count + 1
        print(f"There are {count} absent students")
        c = input("Do you want to continue: ")
        if c == 'yes':
            flag = 1
        else:
            flag = 0
            print("Thanks for using program!!!")

    elif ch == 4:
        realnum = list(filter(lambda x : x > 0, marks))
        i = 0
        max = 0
        for j in realnum:
            if  realnum.index(j)== i:
                if realnum.count(j)>max:
                    max = realnum.count(j)
                    mark = j
            i +=1
        print(f"The mark {mark} with highest frequency max {max} times")
        c = input("Do you want to continue: ")
        if c == 'yes':
            flag = 1
        else:
            flag = 0
            print("Thanks for using program!!!")

    elif ch == 5:
        flag = 0
        print("Thanks for using program")

    else:
        print("Enter valid Choice")
        flag = 1

                    
    
            


        

        