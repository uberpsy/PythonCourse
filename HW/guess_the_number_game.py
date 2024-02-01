import random

print( f'{'*'*21} Levels {'*'*21}' )
print( f'{'* 1. EASY, range: (1, 10), max moves: 7':<49}*' )
print( f'{'* 2. MEDIUM, range: (1, 10), max moves: 5':<49}*' )
print( f'{'* 3. HARD, range: (1, 100), max moves: 10':<49}*' )
print( f'{'*'*50}' )

while True:
    level = int(input('Select level: '))

    match level:
        case 1:
            print("*** Let's play EASY. Good Luck! ***")
            rand_num = random.randint(1, 10)
            sel_range = 10
            tries = 7
            break
        case 2:
            print("*** Let's play Medium. Good Luck! ***")
            rand_num = random.randint(1, 10)
            sel_range = 10
            tries = 5
            break
        case 3:
            print("*** Let's play Hard. Good Luck! ***")
            rand_num = random.randint(1, 100)
            sel_range = 100
            tries = 10
            break
        case _:
            print('Enter a number between 1 and 3')
moves = 1

while tries>0 :
    user_num = int( input( f'\nGuess the number (between 1 and {sel_range}): ' ) )
    

    if user_num > rand_num :
        tries = tries-1
        moves = moves+1
        print( f'Too high! Moves left: {tries}' )
        
    if user_num < rand_num :
        tries = tries-1
        moves = moves+1
        print( f'Too low! Moves left: {tries}' )

    if user_num == rand_num :
        print( f'*** Congratulations! You guessed it right in {moves} moves!. ***' )
        break
