import random
money = 100
HScore = 1000

def money1(money):
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
    again = True
    while again == True:
        again = False
        black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        bett = money1(money)
        money = money - bett
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
            winnings = bett*1.5
        elif bet == "even" and even == True:
            win = True
            winnings = bett*1.5
        elif bet == "red" and color == "red":
            win = True
            winnings = bett*1.5
        elif bet == "black" and color == "black":
            win = True
            winnings = bett*1.5
        elif bet == "1st 12" and (num >= 1 and num <= 12):
            win = True
            winnings = bett*2
        elif bet == "2nd 12" and (num >= 13 and num <= 24):
            win = True
            winnings = bett*2
        elif bet == "3rd 12" and (num >= 25 and num <= 36):
            win = True
            winnings = bett*2
        elif bet == num:
            win = True
            winnings = bett*10
        else:
            win = False
            bett = 0
        print(f"You won £{winnings}")
        money = money+winnings
        money = round(money,2)
        if win == True:
            print(f"the number is {num} {color}, You win!")
            print(f"You have £{money}")
        else:
            print(f"The number is {num} {color}, You lose!")
            print(f"You have £{money}")

        if money > 0:
            again1 = input("Do you want to play again? (y/n)\n")
            if again1 == "y":
                again = True
            else:
                print("Ok")
                again = False
        else:
            again = False


    return money


def BlackJack(money):
    again1 = True
    while again1 == True:
        win = False
        Lose = False
        winnings = 0
        MyCard = []
        H = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        D = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        C = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        S = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        while True:
            amount = 0
            bett = money1(money)
            money = money-bett
            print("first character is the card, second character is the house.\nE.G KH = king of hearts 5C = 5 of clubs")
            while True:
                house = random.randint(1,4)
                if house == 1:
                    house = H
                    name = "H"
                elif house == 2:
                    house = D
                    name = "D"
                elif house == 3:
                    house = C
                    name = "C"
                elif house == 4:
                    house = S
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
                MyCard.append(card+name)
                print(f"Your cards are: {MyCard}")
                print(f"The total is {amount}")
                if amount > 21:
                    print(f"You lost. Your score is {amount}")
                    Lose = True
                    break
                elif amount == 21:
                    print("you win")
                    win = True
                    break
                another = input("Do you want to stick?\nYou wont be able to pick another card! (y/n)\n")
                if another == "y":
                    break
            if win == True:
                winnings = bett * 2
                break
            elif Lose == True:
                bett = 0
                winnings = 0
                break
            else:
                if amount == 19:
                    winnings = bett * 1.4
                elif amount == 20:
                    winnings = bett * 1.6
                break
        money = money+winnings
        money = round(money,2)
        print(f"You won £{winnings}")
        if money <= 0:
            return money
        if money > 0:
            again = input("Do you want to play again? (y/n)\n")
            if again != "y":
                break
                again1 = False

    return money

            
        

            
        
def RPS(money):
    again = True
    winnings = 0
    while again == True:
        winnings = 0
        ai = random.randint(1,1000000000)
        bett = money1(money)
        money = money-bett
        choice = int(input("""
Rock     (1)
Paper    (2)
Scissors (3)
: """))
        #print(ai)
        if (choice == 1 and (ai % 3) == 2) or (choice == 2 and (ai % 3) == 0) or (choice == 3 and (ai % 3) == 1):
            print("You Win")
            winnings = bett*1.8
        elif (choice == 1 and (ai % 3) == 1) or (choice == 2 and (ai % 3) == 2) or(choice == 3 and (ai % 3) == 0):
            print("You lose")
            winnings = 0
            bett = 0
        else:
            print("Draw")
            winnings = bett
        
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
                
        else:
            again = False
            break
    return money
        

while True:
    if money <= 0:
        print("You Broke AF")
        break
    money = round(money,2)
    print(f"You have £{money}")
    print("""
What do you want to play?
- Roulette (1)
- Blackjack (2)
- Rock Paper Scissors (3)
- cash out""")
    game = int(input("- "))
    if game == 1:
        money = roulette(money)
    elif game == 2:
        money = BlackJack(money)
    elif game == 3:
        money = RPS(money)
    elif game == "cash out":
        break

if money > HScore:
    print(f"New High score!\n £{money}")
else:
    print(f"Your score was £{money}")
    print(f"Current High score is £{HScore}")
    
        
        
