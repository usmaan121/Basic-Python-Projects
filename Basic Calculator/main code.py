user_input = float(input("Please enter the first number : "))
operation = input("What do you want to do ? + , - , x , / . : ")
user_input2 = float(input("PLease enter second number : "))

if operation != "+ , - , x , /":
        print("Please select the valid operator") 
elif operation == "+" :
    print(f"The result is : {user_input + user_input2}")
elif operation == "-":
    print(f"The result is : {user_input - user_input2}")
elif operation == "x":
    print(f"The resulr is : {user_input * user_input2}")
elif operation == "/":
    print(f"The result is : {user_input / user_input2}")
else:
    print("Please the valid number")                
