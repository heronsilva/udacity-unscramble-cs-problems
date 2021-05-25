"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

telephone_numbers = set()

for text in texts:
    incoming_number = text[0]
    receiving_number = text[1]

    telephone_numbers.add(incoming_number)
    telephone_numbers.add(receiving_number)

for call in calls:
    incoming_number = call[0]
    receiving_number = call[1]

    telephone_numbers.add(incoming_number)
    telephone_numbers.add(receiving_number)

print("There are {} different telephone numbers in the records.".format(len(telephone_numbers)))
