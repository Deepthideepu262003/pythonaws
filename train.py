Day1=input("Enter a day1  for Python Training Sessions:")
Day2=input("Enter a day2  for Python Training Sessions:")
Day3=input("Enter a day3  for Python Training Sessions:")
Day4=input("Enter a day4  for Python Training Sessions:")
Time1=input("Enter a time for 3 Days")
Time2=input("Enter a time for weekend")

i=1
count=1
while(count<=4):
    if count==1:
        print("The First session is on {0} at {1}".format(Day1,Time1))
        count+=1
    elif count==2:
        print("The Second session is on {0} at {1}".format(Day2,Time1))
        count+=1
    elif count==3:
         print("The Third session is on {0} at {1}".format(Day3,Time1))
         count+=1
    else:
          print("The Fourth session is on {0} at {1}".format(Day4,Time2))
          break;


          
