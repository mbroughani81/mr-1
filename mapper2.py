import sys
import re

def vowel_set(s):
    s = s.lower()
    filtered_chars = list(filter(lambda c: c in "aeiou", s))
    filtered_chars.sort()
    s = "".join(filtered_chars)
    return s

def genKeyValuePairs(line):
    words = line.split()
    # print(words)
    result = list(map(lambda x: (vowel_set(x), 1), words))
    return result

file = open("./input1.txt", mode="r")

# line = sys.stdin.readline()
line = file.readline()

res = ""

while line:
    arr = genKeyValuePairs(line)
    for (key, value) in arr:
        print(key + "\t" + str(value))
    # line = sys.stdin.readline()
    line = file.readline()