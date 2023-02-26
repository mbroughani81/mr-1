import sys
import re
from itertools import combinations

def genKeyValuePairs(line):
    ids = line.replace(":", "").split()
    node = ids[0]
    ids.pop(0) # "node" has edges to all nodes in "ids"

    # for each pair of people in "ids", such as "id1" and "id2", create <id1, id2> as a key-value pair.
    result = list()
    for id1, id2 in list(combinations(ids, 2)):
        result.append((id1, id2))
        result.append((id2, id1))
    return result

def genNeighborPairs(line):
    ids = line.replace(":", "").split()
    node = ids[0]
    ids.pop(0) # "node" has edges to all nodes in "ids"

    # for each person in "ids", such as "id", create <node,id> as a key-value pair.
    result = list()
    for id in ids:
        result.append((node, id))
    
    return result

file = open("./input1.txt", mode="r")

# line = sys.stdin.readline()
line = file.readline()

res = ""

while line:
    # Code description:
    # From every node v, that has a list of neighbors that are in "line" variable,
    # we will create two groups of key-value pairs.
    # first group of key-value pairs:
    # arr is array of (x, y), such x and y are both connected to v. This pair shows that
    # y is suggested to x.
    # If in the end, node b is suggested to node a at least 4 times, 
    # b is in probably list of a. if b is suggested 2 or 3 times, b is in might list of a.
    # In mapper output, we output the key-value pair (x, "s," + y), to show suggesting y to x
    arr = genKeyValuePairs(line)
    for (key, value) in arr:
        print(key + "\t" + "s," + value) # emitting pair used for suggestion
    
    # We also need to know list of neighbors for each node. So for each pairs of node
    # (x, y), we output the (x, "n," + y). In the reducer processing the key x , we will use this information
    # to don't suggest neighbors that are neighbor to x.
    arr = genNeighborPairs(line)
    for (key, value) in arr:
        print(key + "\t" + "n," + value) # emitting pairs to show neighbors
    # line = sys.stdin.readline()
    line = file.readline()