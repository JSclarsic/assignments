#Taurai and Jonathan

import csv
from pprint import pprint

  #Read vegetables.csv into a variable called vegetables.
    

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] 


  #Group vegetables by color as a variable vegetables_by_color.
  

vegetables_by_color = {}
for veggie in vegetables:
    color = veggie['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(veggie)
    else:
        vegetables_by_color[color] = [veggie]

pprint(vegetables_by_color)


  #Output vegetables_by_color into a json called vegetables_by_color.json.
