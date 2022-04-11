#ROCK-PAPER-SCISSOR:

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

your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")

if your_choice != "0" and your_choice != "1" and your_choice != "2":
  print("Hey, Idiot!")
else: 
  if your_choice == "0":
    print(rock)
  elif your_choice == "1":
    print(paper)
  elif your_choice == "2":
    print(scissors)


  import random
  pc_random = random.randint(0, 2)

  if pc_random == 0:
    print(rock)
  elif pc_random == 1:
    print(paper)
  else:
    print(scissors)

  if int(your_choice) == pc_random:
    print("Draw") 
  elif int(your_choice) == 0 and pc_random == 1:
    print("you lose")
  elif int(your_choice) == 1 and pc_random == 2:
    print("you lose")
  elif int(your_choice) == 2 and pc_random == 0:
    print("You lose")
  else:
    print("you win!")