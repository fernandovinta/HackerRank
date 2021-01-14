import sys

i = []
for line in sys.stdin:
    i.append(int(line))
    
print(i[0] // i[1])
print(i[0] % i[1])
print(divmod(i[0], i[1]))
