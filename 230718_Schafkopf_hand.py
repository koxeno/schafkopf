# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:25:32 2023

@author: KeGa3110
"""

class Hand:
    def __init__ (self, cards):
        self.cards = cards
        
    def get_playable_cards (self, suit):
        if suit is None:
            return self.cards
        cards = []
        for card in self.cards:
            if card.binding_suit == suit:
                cards.append (card)
            if len(cards) == 0:
                return self.cards
            return cards
        
    def play (self, card):
        self.cards.remove(card)
        print ("Played Card", card)
        
    def sort (self, game):
        for card in self.cards:
            card.adapt_to(game)
        self.cards.sort()
            
    def evaluate (self, estimator):
        print ("Estimate", [estimator(card) for card in self.cards])
        return sum([estimator(card) for card in self.cards])
    
    def __repr__(self):
        return " ".join([str(x) for x in self.cards])