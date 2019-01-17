#Taurai and Jonathan

#read superheros.json
import json
import csv
from pprint import pprint

with open('superheroes.json', 'r') as f:
	squad = json.load(f)

#write hearder to CSV file

with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])


	#Loop over members and write one row per member

	members = squad['members']
	for member in members:
		name = member["name"]
		age  = member["age"]
		secretIdentity = member["secretIdentity"]
		powers = member["powers"]
		squadName = squad["squadName"]
		homeTown = squad["homeTown"]
		formed = squad["formed"]
		secretBase = squad["secretBase"]
		active = squad["active"]
		writer.writerow([name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active])

