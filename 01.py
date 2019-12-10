import math
data_list = []
calc_data_list = []

## Helper functions to determine fuel consumption based on mass

def fuel_calculator(mass):
  return math.floor(mass/3) - 2

def all_fuel(mass):
  original = fuel_calculator(mass)
  total = original
  additional = fuel_calculator(original)

  while additional > 0:
    if additional > 0:
      total += additional
      additional = fuel_calculator(additional)
    else:
      total = total
      additional = fuel_calculator(additional)

  return total

## operational functions to calculate total fuel demand

with open('./data.txt') as data_file:
  for line in data_file:
      data_list.append(line)

data_list = map(str.strip, data_list)

for item in data_list:
  item = int(item)
  calc_data_list.append(all_fuel(item))

print("The total fuel required is " + str(sum(calc_data_list)))