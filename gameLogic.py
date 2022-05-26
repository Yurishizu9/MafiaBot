import random
import json

print('hi')
def randomly_assign_roles(lobby, roles):
    players = { player : '' for player in lobby}

    for player in lobby:
        player_role = random.choice(roles)
        players[player] = player_role
        roles.remove(player_role)
    return players

def night_time(players, previously_saved = 0):
    mafias = {player: role for player, role in players.items() if role == 'mafia'}
    civilians = {player: role for player, role in players.items() if role != 'mafia'}
    mafias_vote = {}
    victim = ''
    saved = ''

    #<------------------------------
    print(f'\n{mafias}\n{civilians}\n') 
   #------------------------------>

    for name in players:
        # activities for mafia
        role = players[name]
        if role == 'mafia':

            # CHOOSE WHO TO KILL
            #<------------------------------
            print(f'\n{"-"*20} {role}: {name} IT\'S YOUR TURN {"-"*20}\nPrevious mafias voted for {list(mafias_vote)}\nVote a civilian to kill {list(civilians)}\n\n')
            vote = input('\n> ')
            #------------------------------>

            # ADD VICTIM TO LIST
            for player in civilians:
                if vote in player:
                    mafias_vote[player] = 1 if player not in mafias_vote else mafias_vote[player] + 1

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
            input(f'\n{"-"*20} {role}: {name} IT\'S YOUR TURN {"-"*20}\npress ENTER: ')
            pass
            #------------------------------>

        # activity for doctor
        if role == 'doctor':
            #<------------------------------
            input(f'\n{"-"*20} {role}: {name} IT\'S YOUR TURN {"-"*20}\npress ENTER: ')
            pass
            #------------------------------>

        # activity for detective
        if role == 'detective':
            #<------------------------------
            input(f'\n{"-"*20} {role}: {name} IT\'S YOUR TURN {"-"*20}\npress ENTER: ')
            pass
            #------------------------------>

    victim = random.choice(most_voted)
   

    return victim, saved
    #<------------------------------
    print(victim)
    #------------------------------>



#<------------------------------
'''Avoid players with the same name'''
lobby = ['alex1', 'matt2', 'rei3', 'virgil4', 'raf5','martin6'] 
#------------------------------>

# ratio of mafia : civilian 
r_mafia = 2
r_civilian = 3

# total number of mafias and civilians
part = len(lobby) / (r_mafia + r_civilian)
t_mafia = round(part * r_mafia)
t_civilian = round(part * r_civilian)

# total numbers of detective and doctor
t_detective = 0
t_doctor = 0

# create a list of roles for to choose from
t_civilian -= t_doctor + t_detective
roles = ['mafia'] * t_mafia + ['civilians'] * t_civilian + ['detective'] * t_detective + ['doctor'] * t_doctor
#<------------------------------
print(f'Roles: {roles}\n')
#------------------------------>
players = randomly_assign_roles(lobby, roles)
#<------------------------------
mafias = '\u0009'.join([player for player, role in players.items() if role == 'mafia'])
civilians = '\u0009'.join([player for player, role in players.items() if role != 'mafia'])
print(f'MAFIAS:\u0009{mafias}\nCIVILS:\u0009{civilians}\n\n')
#------------------------------>
victim, saved = night_time(players)