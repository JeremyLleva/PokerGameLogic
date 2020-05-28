import itertools
import random
import time

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


"""Creates new Deck"""
def newDeck():
    colors = ['heart', 'diamonds', 'spades', 'clubs']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [Card(value, color) for value in values for color in colors]
    return deck

"""Calculates player hand returns score"""
def check_flush(hand):
    suits = [h.suit for h in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False


def playGame(deck):
    playerHand = deck[:2]
    deck = deck[2:-2]

    computerHand = deck[:2]
    deck = deck[2:-2]

    communityDeck = deck[:3]
    deck = deck[3:-3]

    print("Your Hand")
    print(f"[{playerHand[0].value}, {playerHand[0].suit}], [{playerHand[1].value}, {playerHand[1].suit}]")
    playerHand += communityDeck
    if check_flush(playerHand) == False:
        print("Hand is not a flush")
    else:
        print("Hand is a flush") 

    print("Opponents Hand")
    print(f"[{computerHand[0].value}, {computerHand[0].suit}], [X,X]")

    print("The Flop")

    print(f"[{communityDeck[0].value}, {communityDeck[0].suit}], [{communityDeck[1].value}, {communityDeck[1].suit}], [{communityDeck[2].value}, {communityDeck[2].suit}] [X,X] [X,X]")

deck = newDeck()
random.shuffle(deck)
playGame(deck)
