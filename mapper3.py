import sys
import re
from itertools import combinations

def genKeyValuePairs(line):
    ids = line.replace(":", "").split()
    node = ids[0]
    ids.pop(0) # node has edges to all nodes in ids

    # for each pair of people in ids, such as id1 and id2, create <id1, id2> as a key-value pair.
    result = list()
    for id1, id2 in list(combinations(ids, 2)):
        result.append((id1, id2))
        result.append((id2, id1))
    return result

def genNeighborPairs(line):
    ids = line.replace(":", "").split()
    node = ids[0]
    ids.pop(0) # node has edges to all nodes in ids

    # for each person in ids, such as id, create <node,id> as a key-value pair.
    result = list()
    for id in ids:
        result.append((node, id))
    
    return result

file = open("./input1.txt", mode="r")

# line = sys.stdin.readline()
line = file.readline()

res = ""

while line:
    arr = genKeyValuePairs(line)
    for (key, value) in arr:
        print(key + "\t" + "s," + value) # emitting pair used for suggestion
    arr = genNeighborPairs(line)
    for (key, value) in arr:
        print(key + "\t" + "n," + value) # emitting pairs to show neighbors
    # line = sys.stdin.readline()
    line = file.readline()