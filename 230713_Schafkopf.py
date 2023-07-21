import random
deck= [
    'Aa', '10a', 'Ka', 'Qa', 'Ja', '9a', '8a', '7a',
    'Al', '10l', 'Kl', 'Ql', 'Jl', '9l', '8l', '7l',
    'Ah', '10h', 'Kh', 'Qh', 'Jh', '9h', '8h', '7h',
    'Ab', '10b', 'Kb', 'Qb', 'Jb', '9b', '8b', '7b'
]


random.shuffle (deck)

players = [[], [], [], []]

for i in range (4): 
    players[i] = deck[i * 8: (i + 1) * 8]
    
current_player = 0
tricks = []

for _ in range (8):
    trick = []
    for _ in range (4):
        card = players [current_player].pop(0)
        trick.append (card)
        current_player = (current_player + 1) % 4
        
    tricks.append(trick)

for i, trick in enumerate (tricks):
    print (f"Trick{i + 1}: {','.join(trick)}")  
    
    
    

    
    

