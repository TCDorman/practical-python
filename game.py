import random

print('Wanna play a game?')


#greeting function
def greeting(name):
    print('hello and welcome to the game', name)

#main greeting program
name = input('of course you do, enter your name here:\n')

greeting(name)

#computers random number
def computer_num():
    computer = random.randint(1,100)
    return computer


#game explination
print(name, 'I am thinking of a number between 1 and 100. Guess correctly and you win. Guess incorrectly and see what happens')

computers_number = computer_num()
    
#increase number of guesses
user_guess_count = 1 

#game main function

def game():
    users_guess = int(input("what's your guess?\n"))

    global user_guess_count

    if computers_number > users_guess:
        print(users_guess, 'is too low. try again')
        user_guess_count += 1
        return game()
    elif computers_number < users_guess:
        print(users_guess, "is too high. try again")
        user_guess_count += 1
        return game()
    else: 
        print(str(users_guess), "is correct! Congratulations.", str(user_guess_count)),
        computer_num()
        
    
game()

# print('oops, too high guess again...')
# print('oops, too low guess again...')
# print('you may continue on with your life.')

