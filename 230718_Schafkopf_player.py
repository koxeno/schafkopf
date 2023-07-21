# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:44:31 2023

@author: KeGa3110
"""

from random import SystemRandom as Random

from turn import Turn
from game import Game
from card import Card

class Player:
    def __init__ (self, name, player_id, hand):
        self.name = name
        self.player_id = player_id
        self.hand = hand
        self.stack = []
        self.init_game ()
        
    def __repr__(self)

