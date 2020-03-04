import random
import itertools

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []


        suits = ('\u2660', '\u2663', '\u2665', '\u2666')
        ranks =['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit, rank in itertools.product(suits, ranks):
            self.cards.append(Card(suit, rank))



    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self):
        try:
           return str(self.cards.pop())
        except:
            return "No cards to return"

    def get_random(self):
        try:
            return str(random.choice(self.cards))
        except:
            return "No cards to return"

    def index(self, value):
        try:
            return str(self.cards[int(value)-1])
        except:
            return 'incorrect input'