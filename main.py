#poker game
import random
from collections import Counter
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
rank_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suit_values = {'Clubs':1, 'Diamonds':2, 'Hearts':3, 'Spades':4}
playing = True
#Classes
class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    self.value= rank_values[rank]
    self.suit_rank = suit_values[suit]
  def __str__(self):
    return (f'{self.rank} of {self.suit}')
class Deck:
  def __init__(self):
    self.full_deck = []
    for suit in suits:
      for rank in ranks:
        card = Card(rank, suit)
        self.full_deck.append(card)
  def shuffle(self):
    random.shuffle(self.full_deck)
  def deal(self):
    return self.full_deck.pop()
class Hand:
  def __init__(self):
    self.cards = []
    self.card_value = 0
  def add_card(self,card):
    self.cards.append(card)
class Chips:
  def __init__(self):
    self.total = 100
    self.bet = 0
  def win_bet(self,val):
    self.total += val
  def place_in_pot(self):
    self.total -= self.bet
class Pot:
  def __init__(self):
    self.total = 0
  def add_bet(self,val):
    self.total += val
  def empty_pot(self):
    self.total -= self.total
#bet, fold
def bet(chips):
  while True: 
    try:
      chips.bet = int(input('How much do you want to bet?'))
    except:
      print("number plz")
    else: 
      if chips.bet > chips.total:
        print("You're too broke to afford this amount.")
      else:
        break
def fold(p_bet):
  p_bet.bet = 0
#poker hands
def two_kind(player):
  card_values = []
  for card in player.cards:
    if card.value in card_values:
      return True
    else: 
      card_values.append(card.value)
  return False
def three_kind(player):
  appears = 0
  card_values = []
  for card in player.cards:
    if card.value in card_values:
      appears += 1
      card_values.append(card.value)
    else:
      card_values.append(card.value)
  return appears >= 2
def four_kind(player):
  appears = 0
  card_values = []
  for card in player.cards:
    if card.value in card_values:
      appears += 1
      card_values.append(card.value)
    else:
      card_values.append(card.value)
  return appears >= 3
def two_pair(player):
  pairs = 0
  card_values= []
  for card in player.cards:
    card_values.append(card.value)
  for num in Counter(card_values).values():
    if num == 2:
      pairs += 1
  return pairs == 2
def full_house(player):
  pairs = 0
  triples = 0
  card_values= []
  for card in player.cards:
    card_values.append(card.value)
  for num in Counter(card_values).values():
    if num == 3:
      triples += 1
    elif num == 2:
      pairs += 1
  return triples == 1 and pairs == 1
def high_card(player):
  card_values = []
  for card in player.cards:
    card_values.append(card.value)
  card_values.sort()
  return card_values[-1]  
def suit_rank_measure(player):
  card_values = []
  for card in player.cards:
    card_values.append(card.suit_rank)
  card_values.sort()
  return card_values[-1]/10  
def straight(player):
  card_values = []
  for card in player.cards:
    card_values.append(card.value)
  return sorted(card_values) == list(range(min(card_values),max(card_values)+1))
def flush(player):
  suit_values = []
  for card in player.cards:
    suit_values.append(card.suit_rank)
  for num in Counter(suit_values).values():
    return num == 5
def straight_flush(player):
  conditions = 0 
  card_values = []
  suit_values = []
  for card in player.cards:
    card_values.append(card.value)
    suit_values.append(card.suit_rank)
  for num in Counter(suit_values).values():
    if num == 5:
      conditions += 1
  if sorted(card_values) == list(range(min(card_values),max(card_values)+1)):
    conditions += 1
  return conditions == 2
def royal_flush(player):
  conditions = 0 
  card_values = []
  suit_values = []
  for card in player.cards:
    card_values.append(card.value)
    suit_values.append(card.suit_rank)
  for num in Counter(suit_values).values():
    if num == 5:
      conditions += 1
  if sorted(card_values) == list(range(10,15)):
    conditions += 1
  return conditions == 2  
def show_cards(player):
  print("\nPlayer's Hand:", *player.cards, sep='\n ')
def dealer_cards(player):
  print("\nDealer's Hand:", *player.cards, sep='\n ')
def score_hand(player):
  player_score = [high_card(player)+suit_rank_measure(player)]
  suit_score = suit_rank_measure(player)
  if two_kind(player) == True:
    player_score.append(15+high_card(player)+suit_score)
  if two_pair(player) == True:
    player_score.append(30+high_card(player)+suit_score)
  if three_kind(player) == True:
    player_score.append(45+high_card(player)+suit_score)
  if straight(player) == True:
    player_score.append(60+high_card(player)+suit_score)
  if flush(player) == True:
    player_score.append(75+high_card(player)+suit_score)
  if full_house(player) == True:
    player_score.append(90+high_card(player)+suit_score)
  if four_kind(player) == True:
    player_score.append(105+high_card(player)+suit_score)
  if straight_flush(player) == True:
    player_score.append(120+high_card(player)+suit_score)
  if royal_flush(player) == True:
    player_score.append(135+high_card(player)+suit_score)
  player_score.sort()
  return player_score[-1]
#game logic
print('Welcome to Poker!')
print("It's you against a bot, bot always bets 50, you can bet and fold.")
while True:
  deck = Deck()
  deck.shuffle()
  player_hand = Hand()
  dealer_hand = Hand()
  cash_pot = Pot()
  player_money = Chips()
  player_2_money = Chips()   
  for x in range(5):
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
  bet_turn = True  
  while bet_turn:
    show_cards(player_hand)
    bet_choice = input('bet, or fold?')
    if bet_choice[0].lower()== 'b':
      bet(player_money)
      cash_pot.add_bet(player_money.bet)
    if bet_choice[0].lower()=='f':
      fold(player_money)
    player_money.place_in_pot()
    break
  cash_pot.add_bet(50)
  player_score = score_hand(player_hand)
  show_cards(dealer_hand)
  dealer_score = score_hand(dealer_hand)
  if player_score > dealer_score:
    print('Player wins!')
    player_money.win_bet(cash_pot.total)
  elif dealer_score >= player_score:
    print('Dealer wins!')
  print(f"Player's amount is {player_money.total}")
  if player_money.total == 0:
    print('Oop looks like you splurged all of your money. Good luck with your wife ;)')
    break
  replay = input('play again?')
  if replay.lower()=='y':
    continue
  else:
    print("Thanks for playing!")
    break




    
    



