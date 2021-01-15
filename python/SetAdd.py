# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

stamps = []
for stamp in sys.stdin:
    stamps.append(stamp.strip('\n'))

print(len(set(stamps))-1)
