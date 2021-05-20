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

total_time_by_phone = {}

for call in calls:
    incoming_number = call[0]
    receiving_number = call[0]
    incoming_number_time = int(call[3])
    receiving_number_time = int(call[3])

    if incoming_number not in total_time_by_phone:
        total_time_by_phone[incoming_number] = incoming_number_time
    else:
        total_time_by_phone[incoming_number] += incoming_number_time

    if receiving_number not in total_time_by_phone:
        total_time_by_phone[receiving_number] = receiving_number_time
    else:
        total_time_by_phone[receiving_number] += receiving_number_time

current_longest_time = 0
longest_time_phone_number = {}

for key in total_time_by_phone:
    if total_time_by_phone[key] > current_longest_time:
        current_longest_time = total_time_by_phone[key]
        longest_time_phone_number = {"phone_number": key, "total_time": total_time_by_phone[key]}

print(f"{longest_time_phone_number['phone_number']} spent the longest time, {longest_time_phone_number['total_time']} "
      f"seconds, on the phone during September 2016.")
