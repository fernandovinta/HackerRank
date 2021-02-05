import sys

i = []
for line in sys.stdin:
    i.append(int(line))
    
print(pow(i[0], i[1]))
print(pow(i[0], i[1], i[2]))
