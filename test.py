from collections import Counter

players = {'alex1': 'civilians', 'matt2': 'civilians', 'rei3': 'civilians', 'virgil4': 'mafia', 'raf5': 'civilians', 'martin6': 'civilians'}

x = Counter(players.values())
print(x['mafia'])

print(len(players))