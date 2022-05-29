import random
import json
from collections import Counter 

def randomly_assign_roles(lobby):

    # calculating ratio of mafias and civils
    r_mafia = 1 # ratio of mafia
    r_civilian = 4 # ratio of civilians
    part = len(lobby) / (r_mafia + r_civilian) # ratio formular

    # TOTAL ROLES
    t_detective = 0
    t_doctor = 0
    t_mafia = round(part * r_mafia)
    t_civilian = round(part * r_civilian) - (t_doctor + t_detective) 
    roles = ['mafia'] * t_mafia + ['civilians'] * t_civilian + ['detective'] * t_detective + ['doctor'] * t_doctor
    print(roles)

    # CREATE PLAYERS DICTIONARY
    players = { player : '' for player in lobby}
    for player in lobby:
        player_role = random.choice(roles)
        players[player] = player_role
        roles.remove(player_role)

    #<------------------------------
    mafias = ', '.join([player for player, role in players.items() if role == 'mafia'])
    civilians = ', '.join([player for player, role in players.items() if role != 'mafia'])
    print(f'{"-"*80}\nMAFIAS:\u0009{mafias}\nCIVILS:\u0009{civilians}\n{"-"*80}')
    #------------------------------>

    return players

def night_time(players, previously_saved):
    mafias = {player: role for player, role in players.items() if role == 'mafia'}
    civilians = {player: role for player, role in players.items() if role != 'mafia'}
    mafias_vote = {}
    victim = ''
    saved = ''


    for name in players:
        # activities for mafia
        role = players[name]
        if role == 'mafia':

            # CHOOSE WHO TO KILL
            #<------------------------------
            vote = input(f'\n{role.upper()}: {name}\n{list(civilians)}\nVote a civilian to kill > ')
            #------------------------------>

            # ADD VICTIM TO LIST
            for player in civilians:
                if vote == player:
                    mafias_vote[player] = 1 if vote not in mafias_vote else mafias_vote[player] + 1

            # FIND VICTIM WITH THE HIGHEST VOTE
            highest_number = 0
            most_voted = []
            for name in mafias_vote:
                votes = mafias_vote[name]
                if votes == highest_number:
                    most_voted.append(name) 
                if votes > highest_number:
                    highest_number = votes
                    most_voted.clear()
                    most_voted.append(name)

        # activity for civilians
        if role == 'civilians':
            #<------------------------------
            input(f'\n{role.upper()}: {name}\nNo activities please SKIP > ')
            pass
            #------------------------------>

        # activity for doctor
        if role == 'doctor':
            #<------------------------------
            input(f'\n{role.upper()}: {name}\nNo activities please SKIP > ')
            pass
            #------------------------------>

        # activity for detective
        if role == 'detective':
            #<------------------------------
            input(f'\n{role.upper()}: {name}\nNo activities please SKIP > ')
            pass
            #------------------------------>
    
    if most_voted:
        victim = random.choice(most_voted) 

    
    return victim, saved
    #<------------------------------
    print(victim)
    #------------------------------>

def day_time(players, victim, saved):
    
    # check if victim was saved if not remove them from the game
    # provide a story of the night event
    if victim != saved:
        if victim in players:
            del players[victim]
        print(f'\n{"-"*80}\n~ Last night **{victim}** was killed ~\n{"-"*80}\n') 
    else:
        print(f'\n{"-"*80}\n"~ Last night **nobody** was killed ~\n{"-"*80}\n')

    # DISCUSSION time (90 seconds) - can skip to votes


    # VOTING
    players_vote = {}
    players_list = [name for name in players]
    for name in players:

        # CHOOSE WHO TO VOTE
        #<------------------------------
        players_list.remove(name)
        vote = input(f'\n{name}\n{players_list}\nVote out a Mafia > ')
        players_list.append(name)
        #------------------------------>
        

        # ADD VOTED PLAYER TO VOTE LIST
        for player in players_list:
            if vote == player:
                players_vote[player] = 1 if player not in players_vote else players_vote[player] + 1
    

    # FIND THE MOST VOTED PLAYER
    highest_number = 0
    most_voted = []
    for name in players_vote:
        votes = players_vote[name]
        if votes == highest_number:
            most_voted.append(name) 
            pass
        if votes > highest_number:
            highest_number = votes
            most_voted.clear()
            most_voted.append(name)

    # REMOVE VOTED PLAYER OUT THE GAME
    if len(most_voted) == 1:
        print(f'\n{"-"*80}\nplayers votes: {players_vote}\n{most_voted[0]} was voted out\n{"-"*80}\n')
        del players[most_voted[0]]  
    else: 
        print("Nobody was voted out")
   
    
    # check if mafias are in the game 
    return players
    print(f'\n{"-"*80}')
    print(players)
    print(f'Mafias are still in the game\n{"-"*80}\n')


    
#<------------------------------
'''Avoid players with the same name'''
lobby = ['alex1', 'matt2', 'rei3', 'virgil4', 'raf5','martin6']
#------------------------------>



players = randomly_assign_roles(lobby)
saved = ''

mafia_won = False
civilian_won = False

while not mafia_won or civilian_won:
    victim, saved = night_time(players, saved)

    players = day_time(players, victim , saved)

    # counts how many mafias, civilians, doctors, and detectives are left
    role_counter = Counter(players.values())
    num_mafia = role_counter['mafia']
    num_civilians = round(len(players)/2)

    if 'mafia' not in players.values():
        civilian_won = True
        print('CIVILIANS WON')

    # check if number of mafia == (round(number of all/2))
    if num_mafia >= num_civilians:
        mafia_won = True
        print('MAFIA WON')