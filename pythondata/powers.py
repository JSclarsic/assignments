#Taurai and Jonathan



#Reads superheroes.json 

import json
from pprint import pprint

with open('superheroes.json', 'r') as f:
    squad = json.load(f)



#Creates an empty array called powers

allpowers = []

#Loop thorough the members of the squad,

members = squad['members']
for member in members:

# and append the powers of each to the powers array.

    powers = member['powers']
    for power in powers:
        allpowers.append(power)

#Prints those powers to the terminal

pprint(allpowers)