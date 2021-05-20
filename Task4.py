"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

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

telemarketing_line_number_pattern = r"^140"
possible_telemarketers = []

call_incoming_numbers = []
call_receiving_numbers = []
text_incoming_numbers = []
text_receiving_numbers = []

for call in calls:
    incoming_number = call[0]
    receiving_number = call[1]

    if re.match(telemarketing_line_number_pattern, incoming_number):
        call_incoming_numbers.append(incoming_number)

    call_receiving_numbers.append(receiving_number)

for text in texts:
    incoming_number = text[0]
    receiving_number = text[1]

    text_incoming_numbers.append(incoming_number)
    text_receiving_numbers.append(receiving_number)

for phone_number in call_incoming_numbers:
    if phone_number in call_receiving_numbers \
            or phone_number in text_incoming_numbers \
            or phone_number in text_receiving_numbers:
        continue

    if phone_number not in possible_telemarketers:
        possible_telemarketers.append(phone_number)

sorted_possible_telemarketers_list = sorted(possible_telemarketers)

print("These numbers could be telemarketers:", *sorted_possible_telemarketers_list, sep="\n")
