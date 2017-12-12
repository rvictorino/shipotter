import csv
import random

with open('characters.csv', 'rb') as csvfile:
  characters = csv.reader(csvfile, delimiter=',')
  chars = []
  for char in characters:
    chars.append(char)

  first = chars[random.randint(0, 64)]
  second = chars[random.randint(0, 64)]
  
  print(first[2] + second[3], "(" + first[1] + ", " + second[1] + ")")
