import sys

i = []
for line in sys.stdin:
    i.append(line)

values = i[0].split(" ")
x = values[0]
k = values[1]

print(int(eval(i[1].replace("x", x))) is int(k))
