#/usr/bin/python
from sportmonks import *

token = ''
init(token)


# Leagues

'''
print('Leagues:')
for l in leagues():
	print(l['id'], l['name'])

#gives us the league ID's 
'''
'''
print('Squads:')
for ts in team_squad():
	print(ts['player_id'])

'''

'''

print('Seasons:')
for s in seasons():
	print(s['id'], s['name'],s['league_id'])

#list of seasons in both leauges
'''


print('Teams')
for t in teams(12963):
	print(t['id'],t['name'])
	
'''

print('Squads:')
#for ts in team_squad(12919,1703):
#	print(ts['player_id'])
for t in team_squad(12919,1703):
	print(t['player_id'], player(t['player_id'])['lastname'])

'''
'''
print('Player Data:')
for ts in team_squad(12919,1703):
	print (player(ts['player_id'])['lastname'], ts, '\n')
'''
