import time
import random
import sys

def win() :
    print("THE GAME : You win!")
def lose() :
    print("THE GAME : You lost!")
def draw() :
    print("THE GAME : You draw!")

def game() :
    moves = ['paper', 'rock', 'scissors']
    print("THE GAME : Rock, Paper, or Scissors?")
    attempt=3

    while True :
        if (attempt==0) :
            print("THE GAME : You failed to provide a correct option to play the game. Goodbye.")
            time.sleep(3)
            sys.exit(0)
        player = str(input("Player : ")).lower()
        if player.lower() not in moves :
            print(f'Invalid! You have {attempt} attempts left. Use it wisely.')
            attempt -=1
        else :
            computer = random.choice(moves)
            print(f'\nComputer : {computer}')

            if (computer==player) :
                draw()
            elif (computer=='rock' and player=='paper') :
                win()
            elif (computer=='rock' and player=='scissors') :
                lose()
            elif (computer=='paper' and player=='rock') :
                lose()
            elif (computer=='paper' and player=='scissors') :
                win()
            elif (computer=='scissors' and player=='paper') :
                lose()
            elif (computer=='scissors' and player=='rock') :
                win()
            else :
                pass
            
            ta = str(input('\nTHE GAME : Retry? (y/n) : '))
            if (ta.lower()=='y') :
                game()
            elif (ta.lower()=='n'):
                print("THE GAME is over. Goodbye.")
                time.sleep(3)
                sys.exit(0)
            else :
                print("THE GAME : Invalid.")
                time.sleep(3)
                sys.exit(0)

if __name__ == "__main__":
    game()