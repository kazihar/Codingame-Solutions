import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
result = ''
n = int(raw_input())  # the number of temperatures to analyse
string = raw_input().split()

if (len(string) == 0):
    print("0")
else:
    result = int(string[0])
    
    for i in range(n):
        if (abs(int(string[i])) < abs(result)):
            result = int(string[i])
        elif (abs(int(string[i])) == abs(result)):
            result = max(int(string[i]), result)
print(result)
