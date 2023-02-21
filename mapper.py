import sys
import re

def genKeyValue(line):
	(invoice_no, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country) = line.strip().split(",")

	UnitPrice = float(UnitPrice)
	Quantity = int(Quantity)
	(month, day, year) = InvoiceDate.split("/")

	# (-1, -1) key-value means that row is not valid
	# if first char of InvoiceNo is "C", row is not valid.
	if invoice_no[0] == 'C':
		return ("-1", "-1")
	# if no customer is given, row is not valid.
	if len(CustomerID) == 0:
		return ("-1", "-1")

	total = UnitPrice * Quantity

	key = Country + "," + month
	value = CustomerID + "," + str(total)

	return (key, value)

file = open("./orders.csv", mode="r")


# column_names = sys.stdin.readline()  # column names
column_names = file.readline()

# print(column_names)

# line = sys.stdin.readline()
line = file.readline()

res = ""

while line:
	(key, value) = genKeyValue(line)
	if key != "-1":
		print(key + "\t" + value)
	# line = sys.stdin.readline()
	line = file.readline()
