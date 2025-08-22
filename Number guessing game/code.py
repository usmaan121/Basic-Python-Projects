import random

guess = random.randint(1 , 100)


while True:
    choice = int(input("Enter the number between 1 - 100 :  "))
    if choice < guess:
        print("value is too low")
    elif choice > guess:
        print("value is too high")
    else:
        print("You have choose the correct number")
        break
        
