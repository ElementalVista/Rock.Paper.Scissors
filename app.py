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

#Write your code below this line 👇
import random
random_choice = random.randint(0,2)
computer_options = ['0','1','2']
result = computer_options[random_choice]

choice = input('Which are you going to choose? 0 for Rock, 1 for Paper, 2 for Scissors\n')


#User Choice conditionals
if choice == '0':
    print(rock)
elif choice == '1':
    print(paper)
else:
    print(scissors)

#Computer Choice conditionals
if result == '0':
        print(rock)
elif result == '1':
        print(paper)
else:
        print(scissors)


#Compare user and computer choice for results
if result == '0' and choice =='2':
    print('Computer wins')
elif result =='1' and choice =='2':
    print('You win!')
elif result =='2' and choice =='1':
    print('Computer wins')
elif result =='2' and choice =='0':
    print('You win!')
elif result =='0' and choice =='1':
    print('You win!')
elif result =='1' and choice =='0':
    print('Computer wins')
else:
    print('tie')


#Ending note
print('Thanks for playing!')