import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_royal_flush(self):
    player_hand = Hand()
    card1 = Card('Ten','Clubs')
    card2 = Card('Jack', 'Clubs')
    card3 = Card('King', 'Clubs')
    card4 = Card('Queen', 'Clubs')
    card5 = Card('Ace', 'Clubs')
    player_hand.cards = [card1,card2,card3,card4,card5]
    self.assertEquals(royal_flush(player_hand), True)

  def test_straight_flush(self):
    player_hand = Hand()
    card1 = Card('Two','Clubs')
    card2 = Card('Three', 'Hearts')
    card3 = Card('Four', 'Clubs')
    card4 = Card('Five', 'Clubs')
    card5 = Card('Six', 'Clubs')
    player_hand.cards = [card1,card2,card3,card4,card5]
    self.assertEquals(straight_flush(player_hand), False)

  def test_flush(self):
    player_hand = Hand()
    card1 = Card('Two','Clubs')
    card2 = Card('Two', 'Clubs')
    card3 = Card('Three', 'Clubs')
    card4 = Card('Three', 'Clubs')
    card5 = Card('Two', 'Clubs')
    player_hand.cards = [card1,card2,card3,card4,card5]
    self.assertEquals(flush(player_hand), True)

  def test_score_hand(self):
    player_hand = Hand()
    card1 = Card('Two','Diamonds')
    card2 = Card('Three', 'Hearts')
    card3 = Card('Four', 'Spades')
    card4 = Card('Five', 'Clubs')
    card5 = Card('Six', 'Clubs')
    player_hand.cards = [card1,card2,card3,card4,card5]
    self.assertEquals(score_hand(player_hand), 66.4)

