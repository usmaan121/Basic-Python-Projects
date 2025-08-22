import random

choices = ("r", "p", "s")
while True:
 user = input(("Enter your Choice : (r/p/s)")).lower()
 if user not in choices:
  print("Please enter valid entity")
 computer = random.choice(choices)

 print(f'You choose{[user]}')
 print(f"Computer choose{[computer]}")

 if user == computer:
  print("Match Tie!")

 elif \
  (user == "r" and computer == "s") or\
  (user == "s" and computer == "p") or\
  (user == "p" and computer == "r"):
   print("You win")

 else:
   print("You lose")  
  
 should_continue = input(("Do you want to continue ? (y/n)")).lower()
 if should_continue == "n":
  print("Tnak for playing")
  break
 elif should_continue == "y":
  continue
 else:
  print("Please enter valid entity ")  
   

    
      


       

