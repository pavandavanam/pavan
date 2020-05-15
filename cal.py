# Python program for simple calculator 

# Function to add two numbers 
def add(num1, num2): 
	return num1 + num2 

# Function to subtract two numbers 
def subtract(num1, num2): 
	return num1 - num2 

# Function to multiply two numbers 
def multiply(num1, num2): 
	return num1 * num2 

# Function to divide two numbers 
def divide(num1, num2): 
	return num1 / num2 
      print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")



# Take input from the user 
select = input("Select operations form 1, 2, 3, 4 :") #this referace number given to each operation

number_1 = float(input("Enter first number: "))            #insert a first input value
number_2 = float(input("Enter second number: "))        # second input value
 
if select == '1': 
     print(number_1, "+", number_2, "=", add(number_1, number_2))     

elif select == '2': 
	print(number_1, "-", number_2, "=", subtract(number_1, number_2)) 

elif select == '3': 
	print(number_1, "*", number_2, "=", multiply(number_1, number_2)) 

elif select == '4': 
	print(number_1, "/", number_2, "=", divide(number_1, number_2)) 
else: 
	print("Invalid input") 
