import sys

i = []
for line in sys.stdin:
    i.append(line.replace('\n', ''))
    
l1 = set(i[1].split(" "))
l2 = set(i[3].split(" "))
l3 = l1.union(l2)

print(len(list(l3)))
