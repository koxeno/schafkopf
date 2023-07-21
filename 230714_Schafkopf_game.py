# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:55:25 2023

@author: KeGa3110
"""

import Card

class Game:
    Modes = ["Weiter", "Sauspiel", "Solo", "Wenz"]
    
    def __init__(self, mode, suit = None):
        assert mode in Game.Modes
        assert not suit or suit in Card.Suits #Don't know why assert is used since these are complementary conditions
        
        self.mode = mode
        if self.mode == "Sauspiel":
            self.suit = "h"
            self.called_suit = suit
        else:
            self.suit = suit
            
    def is_trump (self, card):
        if self.mode == "Weiter":
            return False
        elif self.mode == "Wenz":
            return card.number == "U"
        else:
            return card.number in ["O", "U"] or card.suit == self.suit
        
    def __gt__ (self, other):
        if not other:
            return True
        return Game.Modes.index(self.mode) > Game.Modes.index(other.mode)
    
    def __eq__ (self, other):
        if not other:
            return False
        return self.mode == other.mode
    
    def __str__ (self):
        if self.mode == "Sauspiel":
            return self.mode + "with" + Card.Suits[self.called_suit]
        elif self.suit:
            return Card.Suits[self.suit] + " " + self.mode
        else:
            return self.mode
        
    def __repr__ (self):
        if self.suit:
            return self.mode + " " + self.suit
        return self.mode
    
    
        