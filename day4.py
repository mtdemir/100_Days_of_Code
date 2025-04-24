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

list1 = [rock, paper, scissors]
choice1 = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors\n"))
choice2 = random.randint(0, 2)
#choice3 = random.choice(list1)

if choice1 >= 0 and choice1 <= 2:
    print(f'You choose:\n{list1[choice1]}')

print(f'Computer choose:\n{list1[choice2]}')

if choice1==choice2:
    print('It is a draw!')
elif choice1 == 0 and choice2 == 1:
    print('You lose!')
elif choice1 == 0 and choice2 == 2:
    print('You win!')
elif choice1 == 1 and choice2 == 0:
    print('You win!')
elif choice1 == 1 and choice2 == 2:
    print('You lose!')
elif choice1 == 2 and choice2 == 0:
    print('You lose!')
elif choice1 == 2 and choice2 == 1:
    print('You win!')
else:
    print("You typed an invalid number. You lose!")