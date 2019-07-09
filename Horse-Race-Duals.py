import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
pi = []
n = int(input())
for i in range(n):
    pi.append(int(input()))

pi.sort()
diff = 10000000

for i in range(n-1):
    if (diff > abs(pi[i] - pi[i+1])):
        diff = abs(pi[i] - pi[i+1])
        if (diff == 0):
            break
print(diff)
