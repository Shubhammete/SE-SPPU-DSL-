a = int(input("Enter the number of students "))
marks = []
print("Enter the marks of",a,"students")
for i in range(0,a):
    num = int(input())
    marks.append(num)
print('''-------------------------------------------------------''')
print("The marks of ",a,"students")
for i in marks:
    print(i)
flag = 1
while(flag == 1):
    ch = int(input('''
                    1) Average of class
                    2) Highest and Lowest score
                    3) No of students who were absents
                    4) Display marks with highest frequency
                 '''))
    if ch == 1:
        sum = 0
        for i in marks:
            sum =sum + i
        avg = sum/len(marks)
        print("The average of class is",avg)
        c=input("Do you want to continue")
        if c == 'yes':
            flag = 1
        else:
            flag = 0
            print("Thanks for using program!!!")

    
    if ch == 2 :
        marks.sort()
        print("The highest scorer of class is",marks[0])
        print("The lowest scorer of class is",marks[-1])
        c=input("Do you want to continue")
        if c == 'yes':
            flag = 1
        else:
            flag = 0
            print("Thanks for using program!!!")

    if ch == 3:
        count = 0
        for i in marks:
         if marks[i]== "":
            count +=1
        if c == 'yes':
            flag = 1
        else:
            flag = 0
            print("Thanks for using program!!!")

    if ch == 4:
        max = 0
        for j in marks:
            if i == j:
                max=marks.count(i)
                if a < j:
                    max = marks.count(j)
        print("The",j ,"mark with highest frequency",max,"times")

                    
    
            


        

        