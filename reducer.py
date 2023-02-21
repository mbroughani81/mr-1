#!/usr/bin/python3
import sys

big_spenders = set()
big_spender_value = -1

current_key = None
customer_id_to_sum = dict()

def update_customer_id_to_sum(customer_id, p):
    if not customer_id in customer_id_to_sum:
        customer_id_to_sum[customer_id] = 0
    customer_id_to_sum[customer_id] = customer_id_to_sum[customer_id] + p

def format_set(s):
    result = ""
    if len(s) == 0:
        return result
    result = result + s.pop()
    while (len(s)):
        result = result + ", " + s.pop()
    return result

for line in sys.stdin:
    key, value = line.split("\t", 1)
    customer_id, p = value.split(",")
    country, month = key.split(",")
    month = month.rjust(2, "0")
    p = float(p)

    if key == current_key:
        update_customer_id_to_sum(customer_id, p)
    else:
        if current_key != None:
            print(month + "," + country + ":" + format_set(big_spenders))
        big_spenders = set()
        big_spender_value = -1
        current_key = key
        customer_id_to_sum = dict()

        update_customer_id_to_sum(customer_id, p)

    if customer_id_to_sum[customer_id] > big_spender_value:
        big_spenders = set()
        big_spender_value = customer_id_to_sum[customer_id]
        big_spender_id = customer_id
    if customer_id_to_sum[customer_id] == big_spender_value:
        big_spenders.add(customer_id)

if current_key != None:
    print(month + "," + country + ":" + format_set(big_spenders))