
#activity- 1,3
#print("Hello World!")
#this is a comment

#activity- 4
#print("print all the keywords in this python")
#import keyword
#print(keyword.kwlist) 

#Activity 1 
#Name = "Rowanne"
#Age = 13
#print(Name)

#print("my name is {} and my age is {}".format(Name, Age))
#print(f"my name is {Name} and my age is {Age}")
#print("Type of name is", type(Name))
#print("Type of age is", type(Age))
#print("Type of name is", type(Name), "Type of age is", type(Age))

#Age1=24
#age2=str(Age1)
#print("Type of age is", type(age2))

#Activity 2
#num1=45
#num2=3
#print("\nAddition of num1 and num2 is", num1+num2)
#print("Subtraction of num1 and num2 is", num1-num2)
#print("Multiplication of num1 and num2 is", num1*num2)
#print("Division of num1 and num2 is", num1/num2)
#print("Modulus of num1 and num2 is", num1%num2)
#print("Exponent of num1 and num2 is", num1**num2)  
#print("Floor division of num1 and num2 is", num1//num2)

#print("\n num 1 Equal to num2", num1==num2)
#print("num 1 not Equal to num2", num1!=num2)
#print("num 1 greater than num2", num1>num2)
#print("num 1 less than num2", num1<num2)
#print("num 1 greater than or equal to num2", num1>=num2)
#print("num 1 less than or equal to num2\n\n", num1<=num2)

#Activity 3
#First_name="High"
#Last_name="Five"
#Full_name=First_name+""+Last_name
#print("Full name is \n\n", Full_name)

#Word="Codingal"
#print("original word :-")
#print(Word)
#print("Reverse word :-")
#print(Word[::-1])

#print(Word[0:5: 2])

#18/11/2025

#Activity 1
#Odd or Even

#number = int(input("Enter a number : "))
#print(" number is : ", number)

#if number%2==0: 
#   print("number is even")
#else:
#   print("number is odd")

#activity 2
#BMI CALCULATER

#weight = int(input("Enter your weight in kg : "))
#height = float(input("Enter your height in cm : "))
#BMI = weight/(height/100)**2
#print("Your BMI is : ", BMI)

#if BMI<18.5:
# print("You are underweight")
#elif BMI>=18.5 and BMI<24.9:
#  print("You are normal")
#elif BMI>=25 and BMI<29.9:
#  print("You are overweight")
#else:
#   print("you are Obese")

#activity 3
#num=int (input("Enter a number : "))
#if num==50:
#   if num%2==0:
#      print("number is greater than 50 and even")
#   else:
#      print("number is greater than 50 and odd")
#else:
#   print("number is less than 50")
#
#activity 4
#import datetime
#current_time= datetime.datetime.now()
#print('current time is :', current_time)
#print("current time hour is :", current_time.hour)
#print('current time minutes is :', current_time.minute)

#19/11/2025

#activity 1
#for i in range(1,11):
#  print(f"23 x {i} = {23*i}")

#activity 2 

#n= int(input("Enter the number of rows:"))
#for i in range(1,n+1):
#  for j in range(1,i+1):
#    print('*', end="")
#  print()

#activity 3
#total_sum= sum(range(1,11))
#print(f"The sum of fist ten natural numbers is : {total_sum}")

#activity 4
#num = int(input("Enter a number : "))
#if num>1:
#   for i in range(2,num):
#     if (num%i)==0:
#       print (f"{num} is not a prime number")
#       break
#else:
#   print(f"{num} is a prime number")     

#ACTIVITY 1

#lst = ['apple', 'banana', 'fig', 'grape','cherry', 'elderberry']
#print("The original list is :", lst)
#print("The last element of the list is :", len(lst))

#print("The first element of the list is :", lst[0])
#print("The last element of the list is :", lst[5])
#print("The last element of the list is :", lst[-1])

#lst.append("kiwi")
#print("The list after appending kiwi is :", lst)

#lst.remove("fig")
#print("The list after removing fig is :", lst)

#lst.sort()
#print("The list after sorting is :", lst)

#lst.reverse()
#print("The list after reversing is :", lst)

#lst.clear()
#print("The list after clearing is :", lst)
#print(lst)

#activity 2 

#my_dict={
#    "name": "John",
#    "age" : 25,
#    "city" : "New York",
#    "country" : "USA",
#    "email" : "john@example.com",
#    "phone" : "123-456-7890"
#}

#print("The original dicitionary is : ", my_dict)
#print("The value of the key name is : ", my_dict["name"])
#print("The value of the key age is : ", my_dict["age"])

#my_dict["state"] = "New York"
#print("The dictionary after adding state is :", my_dict)

#activity 3

#def test(lst1):
#    result={}
#    for item in lst1:
#        result[item[0]]=item[1:]
#    return result

#student_list = [("John", 25, "New York"), ("Jane", 30, "Los Angeles"),#("Jack", 28, "Chicago")]

#print(test(student_list))
#print("\nOriginal list of lists :", student_list)
#print("Convert the said list of lists to a dictionary : ",student_list)

#ACTIVITY 1 
#my_tuple =()
#print(my_tuple)
#my_tuple = {1,2,3}
#print(my_tuple)

#my_tuple =(1,2,3, "hi")
#print(my_tuple)

#my_tuple =(1,2,3, "hi", 4.5)
#print(my_tuple)

#my_tuple =(1,2,3, "hi")
#print(my_tuple)
#print(my_tuple[0])
#print(my_tuple[1])
#print(my_tuple[2])

#print(my_tuple[0:3])

## ACTIVITY 2
#my_set ={1,2,3,3,4,4,5,5,5,6,7,7,8,9}
#print("my_set", my_set)

#my_set.add(10)
#print("update my_set", my_set)

#set1 = my_set
#set2 = {10,1,2,3,14,15}
#print("differnce :", set1.difference(set2))

## ACTIVITY 3

#setun1 = {"green", "blue"}
#setun2 = {"blue", "yellow"}
#print("union", setun1.union(setun2))

#ACTIVITY 4

#setx ={"apple", "banana"}
#sety ={"banana", "orange"}
#print("intersection", setx.intersection(sety))


# 28/01/2026 #

## Module 14 lesson 1

##Activity 1
#def fun1(n):
 
#  return n*(n+1)/2

#print(fun1(4))

##Activity 2 

#def fun2(n):
#  sum=0
#  for i in range (1,n+1):
#    sum+=i
#  return sum

#print(fun2(4))


#3/2/2026
#activity 1
def printnumber(n):
    iteration=0
    print("the number entered by user is:", n)
    iteration+=1
    print("the number of iteration is :", iteration)

printnumber(10)

#activity 2
def OnTime(n):
    iteration=0
    for i in range(1, n+1):
        iteration+=1
        print("the number of iteration is :", iteration)

OnTime(4)
OnTime(20)

def ONSquareTime(n):
    iteration=0
    for i in range(0, n):
      for j in range(0, n):
          print("*",end="")
          iteration+=1
    print("the number of iteration:", iteration)

ONSquareTime(4)


      
      





