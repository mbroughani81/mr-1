#!/usr/bin/python3
import sys

current_key = None
cnt = 0

for line in sys.stdin:
    key, value = line.split("\t", 1)
    # print(key + " -> " + value)
    if key == current_key:
        cnt = cnt + 1
    else:
        if current_key != None:
            # print result
            print(current_key + ":" + str(cnt))
        # start reading new key
        current_key = key
        cnt = 1

if current_key != None:
    print(current_key + ":" + str(cnt))
