#!/usr/bin/python3
import sys

current_key = None
neighbors = list()
suggestion_count = dict() # suggestion_count[x] shows the number of times x is suggested to current key.

def print_list(l):
    if len(l) == 0:
        return
    print(l.pop(0), end="")
    while len(l) > 0:
        print("," + str(l.pop(0)), end="")

def print_result():
    might_list = list()
    # suggestion_count.items() return all key values in suggestion_count. 
    # might_list will have all the "id"s that their count in map is 2 or 3.
    for id, cnt in suggestion_count.items():
        if cnt == 2 or cnt == 3:
            might_list.append(id)
    # we need to exclude the neighbors in might list
    might_list = list(filter(lambda x: x not in neighbors, might_list))
    might_list.sort()

    # probably_list will have all the "id"s that their count in map is 2 or 3.
    probably_list = list()
    for id, cnt in suggestion_count.items():
        if cnt >= 4:
            probably_list.append(id)
    # we need to exclude the neighbors in might list
    probably_list = list(filter(lambda x: x not in neighbors, probably_list))
    probably_list.sort()

    print(current_key + ":", end="")
    if len(might_list) > 0:
        print("Might(", end="")
        print_list(might_list)
        print(")", end="")
    print(" ", end="")
    if len(probably_list) > 0:
        print("Probably(", end="")
        print_list(probably_list)
        print(")", end="")
    print()

for line in sys.stdin:
    key, value = line.split("\t", 1)

    type, id = value.strip().split(",")
    id = int(id)
    # print(key + " -> " + type + " " + id)

    # check if new key is started
    if key != current_key: # new key is started
        if current_key != None:
            print_result()
        current_key = key
        # reset neighbors and suggestion_count
        neighbors = list()
        suggestion_count = dict()
    
    if type == "n":
        neighbors.append(id)
    if type == "s":
        # if a suggestion happened for "id" for first time, set suggestion_count[id] to 0 
        if not id in suggestion_count:
            suggestion_count[id] = 0
        # increase count of suggestion
        suggestion_count[id] = suggestion_count[id] + 1
if current_key != None:
  print_result()