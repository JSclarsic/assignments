#Taurai and Jonathan


#Read vegetables.csv into a variable called vegetables.
import json
import csv
from pprint import pprint

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] 



#Loop through vegetables and filter down to only green vegtables using a whitelist.

greenvegetables = []
whitelist = ['green']
for veggie in vegetables:
    if veggie['color'] in whitelist:
        greenvegetables.append(veggie)

#Print veggies to the terminal

pprint(greenvegetables)

#Write the veggies to a json file called greenveggies.json




with open('greenveggies.json', 'w') as f:
    json.dump(greenvegetables, f)