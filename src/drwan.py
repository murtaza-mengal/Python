
import random 
computer = random.randint(0,4)
user = int(input())
print(f"Your pick:{user}")
print(f" Computer:{computer}")

win = [user == 0 and computer == 2 or user == 2
and computer == 1 or user == 1 and computer == 0
or user == 0 and computer == 4 or user == 4 and
computer == 3 or user == 3 and computer == 2
or user == 4 and computer == 1 or user == 3 
and computer == 0 or user == 2 and computer 
== 4 or user == 1 and computer == 3]


if any(win):
  print("You Won 😎")
elif(user == computer):
  print("Match Drawn 🗿")
else:
  print("Computer Won 🤯")
    
"""
Enter a integer 0 - 4 to play
user input: 0 = rock
            1 = paper 
            2 = scissor 
            3 = spock 
            4 = lizard 

Rules: rock crushes scissor 
       scissor cuts paper 
       paper covers rock
       rock smashes lizard
       lizard poisons spock
       spock smashes scissor 
       lizard eats paper 
       spock vaporises rock
       scissor decapitates lizard 
       paper disproves spock
             
"""