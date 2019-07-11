import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lonA = input()
latA = input()
defibs = []
n = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
def convert_to_float(value):
    return (float(value.replace(',', '.')))

def distance(lonB, latB, lonA, latA):
    lonB = convert_to_float(lonB)
    latB = convert_to_float(latB)
    lonA = convert_to_float(lonA)
    latA = convert_to_float(latA)
    x = (lonB - lonA) * math.cos((latA + latB) / 2)
    y = (latB - latA)
    d = math.sqrt(x * x + y * y) * 6371
    return d

for i in range(n):
    defib = input()
    split_defib = defib.split(';')
    defib_data = {
        'id': int(split_defib[0]),
        'name': split_defib[1],
        'add': split_defib[2],
        'no': split_defib[3],
        'lonB': split_defib[4],
        'latB': split_defib[5],
        }
    defibs.append(defib_data)

min_distance = None
nearest_defib = {}

if (len(defibs) > 1):
    for i in defibs:
        d = distance(i['lonB'], i['latB'], lonA, latA)
        if (min_distance is None):
            min_distance = d
            nearest_defib = i
        elif (d < min_distance):
            min_distance = d
            nearest_defib = i
else:
    nearest_defib = defibs[0]

print(nearest_defib['name'])
