razpolozenje = input ('What is your mood: ')

if razpolozenje == 'happy':
    print ('Great to see you happy!')
elif razpolozenje == 'nervous':
    print('Relax, everything will be alright.')
elif razpolozenje == 'sad':
    print('I hope i can cheer you up.')
elif razpolozenje == 'excited':
    print('Me as well.')
elif razpolozenje == 'relaxed':
    print('Great.')
else:
    print('I do not recognize this mood.')



# 2. Domaca naloga


secret = 5
print("Casino game")
print("Guess a number from 0 - 5")
guess = int(input("Type your number: "))
if secret == guess:
    print("Congratulations, the number is correct. You won the jackpot!")
elif 4 == guess:
    print("You were so close, better luck next time!")
elif  3 == guess:
    print("Wrong number, try again!")
elif 2 == guess:
    print("Incorrect number, better luck next time!")
else:
    print("Sorry, better luck next time.")



# 3. Domaca naloga

print("Calculator")

first_num = int(input("enter the first number: "))
second_num = int(input("enter the second number: "))
operation = input("Arithmetic operation: ")

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    print(first_num / second_num)