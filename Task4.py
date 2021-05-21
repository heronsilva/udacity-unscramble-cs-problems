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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = []
called = []
texters = []
texted = []

for call in calls:
    incoming_call_number = call[0]
    receiving_call_number = call[1]

    if incoming_call_number not in callers:
        callers.append(incoming_call_number)

    called.append(receiving_call_number)

for text in texts:
    incoming_text_number = text[0]
    receiving_text_number = text[1]

    texters.append(incoming_text_number)
    texted.append(receiving_text_number)

for phone_number in callers[:]:
    if phone_number in called or phone_number in texters or phone_number in texted:
        callers.remove(phone_number)

possible_telemarketers = sorted(callers)

print("These numbers could be telemarketers:", *possible_telemarketers, sep="\n")
