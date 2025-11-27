un = "This was unsucsessfull."
suc = "This was successfull."

#print("For declaring a function, we use the 'def' keyword \n")

#def sample_fun():
#    print("This is a sample function")

#print(un)

#print("If we want our function to return some value,")
#print("We can do that using the'return' key word")

#def sample_fun():
#    a = 5
#    print("This is a sample function")
#    return a

#print(un)

#print("To execute a block of code written inside the function, we have to call it as well; defining it is not enough.")
#print("To call a function, use the name of the function, followed by () parenthesis")

#def sample_fun():
#    a = 5
#    print("This is a sample function...")
#    return a 

#sample_fun()

#print(un)

#print("The value returned by this function needs to be stored as well while calling for using it.")

#def sample_fun():
#    a = 5
#    print("This is a sample function...")
#    return a

#b = sample_fun()
#print(b)

#print(suc)

#print("Parameters are the information/values passed to the function to be used anywhere in function.")
#print("They are specified inside the parameters while calling the fuction.")

#def sample_fun(name):
#    print("This is a sample function of", name)

#sample_fun("LilacSpecter")

#print(suc)

#print("Recursion is the process of defining something in terms of itself.")
#print("A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recusively.")

#def recurse():
#    ...
#    recurse()
#    ...

#recurse()

#print()

#ACTIVITY 1///
#print("Introduce Yourself")

#def intro(name):

#    print("Hello, Good morning! I am",name)

#user_name = input("Enter your name")
#intro(user_name)
    
#ACTIVITY 2///
print("Factorial")

#Factorial of a number using recursion 
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

num = int(input("Enter a number"))

# check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))

#ACTIVITY 3///
print("Calculator")

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

#This function subtracts two numbers
def subtract(x, y):
    return x - y

#This function multiplies two numbers 
def multiply(x, y):
    return x * y

#This function divides two numbers
def divide(x, y):
    return x / y

num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))

print("Sum :", add(num1, num2))
print("Defference :", subtract(num1, num2))
print("Product :", multiply(num1, num2))
print("Quotient :", divide(num1, num2))

print("Thank you, and we are done!!!!")