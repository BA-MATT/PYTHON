import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock,paper,scissors]
#x=random.choice(game)
#x=random.randint(0,len(game)-1)
x=random.randint(0,2)

user_input =int(input(" Please enter the choice 0 - ROCK, 1 - PAPER, 2 - SCISSORS  : "))
#print (game[x])

if x == 0 and user_input ==1:
    print("Computer has selected SCISSORS")
    print(game[0])
    print("You have selected PAPER")
    print(game[1])
    print ("COMPUTER WINS....!!")

elif x == 1 and user_input ==2:
    print("Computer have selected PAPER")
    print(game[1])
    print("You has selected ROCK")
    print(game[2])
    print ("COMPUTER WIN.....!!")

elif x == 2 and user_input ==1:
    print("Computer have selected ROCK")
    print(game[2])
    print("You has selected SCISSORS")
    print(game[1])
    print ("COMPUTER WIN....!!")
#*****************************
elif user_input == 0 and x ==1:
    print("You have selected SCISSORS")
    print(game[0])
    print("Computer has selected PAPER")
    print(game[1])
    print ("YOUUUU WINNN....!!")

elif user_input == 1 and x ==2:
    print("You have selected PAPER")
    print(game[1])
    print("Computer has selected ROCK")
    print(game[2])
    print ("YOUUUU WINNN....!!")

elif user_input == 2 and x ==1:
    print("You have selected ROCK")
    print(game[2])
    print("Computer has selected SCISSORS")
    print(game[1])
    print ("YOUUUU WINNN....!!")

elif user_input == x:
    print("You and compuetr selected same")
    print(game[x])

else:
    print ("Invalid Input")