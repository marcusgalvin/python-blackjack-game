# random number generator by calling random.choice
import random


deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
        9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

user_card1 = []
user_card2 = []
user_card3 = []
user_card4 = []
user_card5 = []


dealer_card_up = []

dealer_card_down = []

next_draw = []


def main():

    print("Marcus' BlackJack Simulator")

    print("Good Luck, The total amout of cards in the deck is: ", len(deck))

    # first deal two random cards to the user

    user_card1 = random.choice(deck)
    # after the random card is delt to the user, pop the users card off the deck
    deck.pop(user_card1)

    user_card2 = random.choice(deck)
    deck.pop(user_card2)

    print("Users 1st card is:", user_card1)
    print("Users 2nd card is: ", user_card2)
    print("--------------------------")

    # if user hits 21 on first deal, end game
    if user_card1 + user_card2 == 21:
        print("Congratz, you hit black jack!")
        exit()

    # next deal the dealer two cards but only diplay one
    dealer_card_up = random.choice(deck)
    deck.pop(dealer_card_up)

    dealer_card_down = random.choice(deck)
    deck.pop(dealer_card_down)

    print("Dealer's Cards: ", dealer_card_up, dealer_card_down)
    print("--------------------------")

    # if computer hits blackjack game over
    if dealer_card_up + dealer_card_down == 21:
        print("Game Over, the computer hit blackjack")
        exit()

    # ask the use if they want to hit
    next_draw = input("Type 1 to stay and 2 to hit: ")
    if next_draw == 2:
        print("User has chosen to hit")
        user_card3 = random.choice(deck)
        deck.pop(user_card3)
        print("Users 1st card is:", user_card1)
        print("Users 2nd card is:", user_card2)
        print("Users 3rd card is:", user_card3)

    elif next_draw != 2:
        print("User has chosen to stay")

    # if user hits and goes over 21, they loose program exits
    if user_card1 + user_card2 + user_card3 > 21:
        print("Sorry, thats a bust!")
        exit()
    # if user hits blackjack at 21, they win
    if user_card1 + user_card2 + user_card3 == 21:
        print("Congratz, you hit Blackjack!")
        exit()

    elif user_card1 + user_card2 + user_card3 <= 21:

        # ask hit/ stay again -- card 4
        next_draw = input("Type 1 to stay and 2 to hit: ")

    if next_draw == 2:
        print("User has chosen to hit")
        user_card4 = random.choice(deck)
        deck.pop(user_card4)
        print("Users 1st card is:", user_card1)
        print("Users 2nd card is:", user_card2)
        print("Users 3rd card is:", user_card3)
        print("Users 4th card is:", user_card4)

    elif next_draw != 2:
        print("User has chosen to stay")

    # if user hots over 21, bust
    if user_card1 + user_card2 + user_card3 + user_card4 > 21:
        print("Sorry, thats a bust!")
        exit()

    # if user hits blackjack at 21, they win
    if user_card1 + user_card2 + user_card3 + user_card4 == 21:
        print("Congratz, you hit Blackjack!")
        exit()

    elif user_card1 + user_card2 + user_card3 + user_card4 <= 21:

        # card 5 prompt hit/stay -----------------------------------
        next_draw = input("Type 1 to stay and 2 to hit: ")

        if next_draw == 2:
            print("User has chosen to hit")
        user_card5 = random.choice(deck)
        deck.pop(user_card5)
        print("Users 1st card is:", user_card1)
        print("Users 2nd card is:", user_card2)
        print("Users 3rd card is:", user_card3)
        print("Users 4th card is:", user_card4)
        print("Users 5th card is:", user_card5)

    elif next_draw != 2:
        print("User has chosen to stay")

    if user_card1 + user_card2 + user_card3 + user_card4 + user_card5 > 21:
        print("Sorry, thats a bust!")
        exit()

    # if user hits blackjack at 21, they win
    if user_card1 + user_card2 + user_card3 + user_card4 + user_card5 == 21:
        print("Congratz, you hit Blackjack!")
        exit()

    elif user_card1 + user_card2 + user_card3 + user_card4 <= 21:
        next_draw = input("Type 1 to stay and 2 to hit: ")


if __name__ == "__main__":
    main()
