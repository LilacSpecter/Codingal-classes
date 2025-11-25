
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