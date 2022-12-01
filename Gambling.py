import random
import os
money = 100
hscore = 1000
os.system('cls')

print("""
_  _  _  ____""")

def reset():
    playAgain = input("Do you want to play again? (y/n)")
    if playAgain == "y":
        replay = True
    else:
        replay = False
    return replay

def betting(money):
    while True:
        print(f"You have £{money}")
        amount = float(input("How much money are you betting?\n£"))
        if amount > money:
            print("You dont have that much money!\n Try again")
        elif amount < 1 and (money - amount) != 0:
            print("You cant bet less than £1")
        elif ((money - amount) < 1) and ((money - amount) != 0):
            print("You need to save yourself £1 minimum\n Or go all out!")
        elif amount <= 1000:
            break
        elif amount == 0:
            print("You cant bet £0")
        else:
            print("You can only bet £1-1000")
    return amount
    
def roulette(money):
    black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    betAmount = betting(money)
    money = money - betAmount
    winnings = 0
    bet = input("""
You can bet on:
a number from 1 - 36,
the colours red or black,
and odd or even.
You can also bet on:
1st 12 (1-12)
2nd 12 (13-24)
3rd 12 (25-36)
Choose one of them:
""")
    num = random.randint(1,36)
#finding color
    if num in black:
        color = "black"
    else:
        color = "red"
#Finding even or odd
    if num % 2 == 0:
        even = True
    else:
        even = False
#Calculating bets
    if bet == "odd" and even == False:
        win = True
        winnings = betAmount*1.5
    elif bet == "even" and even == True:
        win = True
        winnings = betAmount*1.5
    elif bet == "red" and color == "red":
        win = True
        winnings = betAmount*1.5
    elif bet == "black" and color == "black":
        win = True
        winnings = betAmount*1.5
    elif bet == "1st 12" and (d >= 1 and d <= 12):
        win = True
        winnings = betAmount*2
    elif bet == "2nd 12" and (d >= 13 and d <= 24):
        win = True
        winnings = betAmount*2
    elif bet == "3rd 12" and (num >= 25 and num <= 36):
        win = True
        winnings = betAmount*2
    elif bet == num:
        win = True
        winnings = betAmount*10
    else:
        win = False
        betAmount = 0
    print(f"You won £{winnings}")
    money = money+winnings
    money = round(money,2)
    if win == True:
        print(f"the number is {num} {color}, You win!")
        print(f"You have £{money}")
    else:
        print(f"The number is {num} {color}, You lose!")
        print(f"You have £{money}")
    return money


def BlackJack(money):
    win = False
    lose = False
    winnings = 0
    myCard = []
    heart = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    diamond = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    club = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    spade = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    while True:
        amount = 0
        betAmount = betting(money)
        money = money-betAmount
        print("first cheartaracter is the card, second character is the house.\nE.G KH = king of hearts 5C = 5 of clubs")
        while True:
            house = random.randint(1,4)
            if house == 1:
                house = heart
                name = "H"
            elif house == 2:
                house = diamond
                name = "D"
            elif house == 3:
                house = club
                name = "C"
            elif house == 4:
                house = spade
                name = "S"
            card = random.choice(house)
            if card == "A":
                choose = int(input("Do you want your Ace to be 1 or 11?\n"))
                if choose == 1:
                    amount += 1
                else:
                    amount += 11
            elif card == "2":
                amount += 2
            elif card == "3":
                amount += 3
            elif card == "4":
                amount += 4
            elif card == "5":
                amount += 5
            elif card == "6":
                amount += 6
            elif card == "7":
                amount += 7
            elif card == "8":
                amount += 8
            elif card == "9":
                amount += 9
            elif card == "10":
                amount += 10
            elif card == "J":
                amount += 10
            elif card == "Q":
                amount += 10
            elif card == "K":
                amount += 10
            house.remove(card)
            myCard.append(card+name)
            print(f"Your cards are: {myCard}")
            print(f"The total is {amount}")
            if amount > 21:
                print(f"You lost. Your score is {amount}")
                lose = True
                break
            elif amount == 21:
                print("you win")
                win = True
                break
            another = input("Do you want to stick?\nYou wont be able to pick another card! (y/n)\n")
            if another == "y":
                break
        if win == True:
            winnings = betAmount * 2.5
            break
        elif lose == True:
            betAmount = 0
            winnings = 0
            break
        else:
            if amount == 18:
                winnings = betAmount * 1.25
            elif amount == 19:
                winnings = betAmount * 1.5
            elif amount == 20:
                winnings = betAmount * 2
            else:
                winnings = betAmount
                break
        money = money+winnings
        money = round(money,2)
        print(f"You won £{winnings}")
        
    return money

            
        

            
        
def RPS(money):
    winnings = 0
    ai = random.randint(1,1000000000)
    bet = betting(money)
    money = money-bet
    choice = int(input("""
Rock     (1)
Paper    (2)
Scissors (3)
: """))
    #print(ai)
    if (choice == 1 and (ai % 3) == 2) or (choice == 2 and (ai % 3) == 0) or (choice == 3 and (ai % 3) == 1):
        print("You Win")
        winnings = bet*1.8
    elif (choice == 1 and (ai % 3) == 1) or (choice == 2 and (ai % 3) == 2) or(choice == 3 and (ai % 3) == 0):
        print("You lose")
        winnings = 0
        bet = 0
    else:
        print("Draw")
        winnings = bet
        
    money = money + winnings
    money = round(money,2)
    print(f"You have £{money}")
    if money > 0:
        again1 = input("Do you want to play again? (y/n)\n")
        if again1 == "y":
            again = True
        else:
            print("Ok")
            again = False
                
    return money
        

while True:
    if money <= 0:
        print("You Broke AF")
        break
    money = round(money,2)
    print(f"You have £{money}")
    print("""
What do you want to play?
- Roulette\t\t(1)
- Blackjack\t\t(2)
- Rock Paper Scissors\t(3)
- cash out\t\t(4)""")
    game = int(input("- "))
    if game == 1:
        while reset() == True:
            money = roulette(money)
    elif game == 2:
        while reset() == True:
            money = BlackJack(money)
    elif game == 3:
        while reset() == True:
            money = RPS(money)
    elif game == 4:
        break

if money > hscore:
    print(f"New High score!\n £{money}")
else:
    print(f"Your score was £{money}")
    print(f"Current High score is £{hscore}")
    
        
        
