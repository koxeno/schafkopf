# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 17:05:11 2023

@author: KeGa3110
"""

class Card:
    Suits = {
        "e": "Eichel",
        "g": "Gras",
        "h": "Herz",
        "s":"Schell"
        }
    Numbers = {
     "A": "Ace",
     "10": "Zehn",
     "K": "König",
     "O": "Ober",
     "U": "Unter",
     "9": "Neun",
     "8": "Acht",
     "7": "Sieben"
        }
    
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.binding_suit = suit
        
        if number in ["O", "U"] or suit == "h":
            self.binding_suit = "t"
            
    def __repr__(self): 
        return self.suit + "+" + self.number
    
    def __str__(self):
        return self.suit + "-" + self.number
    
    def order(self):
        return self.suit + "-" + str(Card.Numbers.index(self.number))
    
    def binding_order(self):
        return self.binding_suit + "-" + str(Card.Numbers.index(self.number))
    
    def adapt_to (self, game):
        if game.is_trump (self):
            self.binding_suit = "t"
        else: 
            self.binding_suit = self.suit
            
    def __lt__(self, other):
        if (self.binding_suit == "t") ^ (other.binding_suit == "t"): 
            return self.binding_suit == "t"
        elif self.binding_suit == "t":
            if (self.number == "O") ^(other.number == "O"):
                return self.number == "O"
            elif (self.number == "U") ^ (other.number == "U"):
                return self.number == "U"
            return self.order() < other.order() 
        else:
            return self.binding_order() < other.binding_order()
        
    def __gt__(self, other):
        if (self.binding_suit == "t") or (other.binding_suit == "t") or (self.binding_suit == other.binding_suit):
            return self < other
        else:
            return False
        
    def __eq__ (self, other):
        return self.__repr__() == other.__repr__()
    
    def __le__ (self, other): 
        return self < other or self == other
    
    def __ge__(self, other):
        return self > other or self == other
    
    
                
            
    
    
    
        
        