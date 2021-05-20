"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_time_by_phone = {}

for call in calls:
    incoming_number = call[0]
    receiving_number = call[1]

    incoming_number_time = int(call[3])
    receiving_number_time = int(call[3])

    if incoming_number not in call_time_by_phone:
        call_time_by_phone[incoming_number] = incoming_number_time
    else:
        call_time_by_phone[incoming_number] += incoming_number_time

    if receiving_number not in call_time_by_phone:
        call_time_by_phone[receiving_number] = receiving_number_time
    else:
        call_time_by_phone[receiving_number] += receiving_number_time

max_time_spent = max(call_time_by_phone, key=call_time_by_phone.get)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
    max_time_spent, call_time_by_phone.get(max_time_spent)))
