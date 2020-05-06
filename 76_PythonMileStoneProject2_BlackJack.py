import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.deck = [] # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        n = 1
        for i in range(len(self.deck)):
            print(f'{n}: {self.deck[i]}')
            n += 1

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card

class Hand:
    def __init__(self):
        self.cards = [] # start with empty hand
        self.value = 0 # start with zero value on hand
        self.aces = 0 # start with zero aces on hand
        #global suits
        #global ranks
        #global values

    def __str__(self):
        cardlist = []
        for i in range(len(self.cards)):
            cardlist.append(self.cards[i].__str__())
        return f'Cards in hand: {cardlist}\n' \
               f'Card value in hand: {self.value}\n' \
               f'Aces in hand: {self.aces}\n'

    def add_card(self, card):
        self.cards.append(card)
        self.value += values.get(card.rank)

# THIS CODE BELOW MIGHT NEED TO BE FURTHER TESTED ON THE GAME PLAY
    def adjust_for_ace(self):
        for i in range(len(self.cards)):
            if self.cards[i].rank == 'Ace':
                self.aces += 1
                if self.value > 21:
                    self.value -= 10

# testing code for Deck Class
#mydeck = Deck()
#mydeck.shuffle()
#mycard = mydeck.deal()
#mydeck.__str__()

# testing code for Hand Class
#player_hand = Hand()
#player_hand.add_card(mydeck.deal())
#print(player_hand.value)
#player_hand.add_card(mydeck.deal())
#player_hand.add_card(mydeck.deal())
#print(player_hand.value)
#player_hand.adjust_for_ace()
#print(player_hand.value)
#print(player_hand.aces)
#print(player_hand)

class Chips:

    def __init__(self):
        self.total = 100 # Starting chips total by default
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet():
    bet = ''
    while type(bet) is not int:
        try:
            bet = int(input("Place your bet: "))
            return bet
        except ValueError:
            print("Value must be integer")
    return bet

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing # to control an upcoming while loop
    answer = ''
    while (answer != 'hit') or (answer != 'stand'):
        answer = input("Hit or stand? ").lower()
        if answer == 'hit':
            hit(deck, hand)
            break
        elif answer == 'stand':
            playing = False
            break
        else:
            print("input not understood")

# testing code for hit_or_stand function
# mydeck = Deck()
# mydeck.shuffle()
# myhand = Hand()
# myhand.add_card(mydeck.deal())
# myhand.adjust_for_ace()
# myhand.add_card(mydeck.deal())
# myhand.adjust_for_ace()
# myhand.add_card(mydeck.deal())
# myhand.adjust_for_ace()
# print(myhand)
# hit_or_stand(mydeck, myhand)
# print(myhand)

# FUNCTION TO DISPLAY CARDS
def show_some(player, dealer):  # THIS ONE NEED TO BE TESTED FURTHER
    print("Player's cards:")
    for i in range(len(player.cards)):
        print(player.cards[i])
    print("\nDealer's card:")
    print(dealer.cards[0])

def show_all(player, dealer):
    print("Player's cards:")
    for i in range(len(player.cards)):
        print(player.cards[i])
    print("\nDealer's cards:")
    for i in range(len(dealer.cards)):
        print(dealer.cards[i])

# code for testing show_some and show_all function
# mydeck = Deck()
# mydeck.shuffle()
# player_hand = Hand()
# player_hand.add_card(mydeck.deal())
# player_hand.add_card(mydeck.deal())
# dealer_hand = Hand()
# dealer_hand.add_card(mydeck.deal())
# dealer_hand.add_card(mydeck.deal())
# show_some(player_hand, dealer_hand)
# show_all(player_hand, dealer_hand)

# THIS FUNCTIONS BELOW WILL BE HANDLING THE END GAME SCENARIOS

def player_busts(player, dealer, chips):
    print("Player busted!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player win!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busted! Player win!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer win!")
    chips.lose_bet()

def push(player, dealer):
    print("Player and dealer tie!")

if __name__ == '__main__':
    playing = True
    border = '===================='
    while True:
        # Print an opening statement
        print(border)
        print("WELCOME TO BLACK JACK")
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        player = Hand()
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        dealer = Hand()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())

        # Set up the Player's chips
        chips = Chips()
        print(f'Your total chips: {chips.total}')

        # Prompt the Player for their bet
        chips.bet = take_bet()
        while chips.bet > chips.total:
            print("Your bet could not exceeds your available chips")
            chips.bet = take_bet()

        # Show cards (but keep one dealer card hidden)
        print(border)
        show_some(player, dealer)
        print(border)

        while playing: # recall this variable from our hit_or_stand function
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player)
            # Show cards (but keep one dealer cars hidden)
            print(border)
            show_all(player, dealer)
            print(border)
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.value > 21:
                player_busts(player, dealer, chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            else:
                while dealer.value <= 17:
                    hit(deck, dealer)
                    print("Dealer HIT!")
            # Show all cards
            print(border)
            show_all(player, dealer)
            print(border)

            # Run different winning scenarios
            if dealer.value > 21:
                dealer_busts(player, dealer, chips)
            elif dealer.value > player.value:
                dealer_wins(player, dealer, chips)
            elif dealer.value < player.value and player.value <= 21:
                player_wins(player, dealer, chips)
            else:
                push(player, dealer)

        # Inform Player of their chips total
        print(f'your total chips: {chips.total}')
        # Ask to play again
        answer = input("Wanna play again? (y/n) ")
        if answer.lower() == 'y':
            playing = True
            continue
        if answer.lower() == 'n':
            playing = False
            break
        else:
            answer = input("Wanna play again? (y/n) ")

            break