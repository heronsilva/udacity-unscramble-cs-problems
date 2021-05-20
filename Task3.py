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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

bangalore_fixed_area_code_pattern = r"^\(080\)"

fixed_line_number_pattern = r"^\(0\d+\)"
fixed_line_area_code_pattern = r"^\((0\d+)\)"

mobile_line_number_pattern = r"^(7|8|9)\d+\s\d+"
mobile_line_area_code_pattern = r"^(\d{4})"

telemarketing_line_number_pattern = r"^140"
telemarketing_line_area_code_pattern = r"(^140)"

codes_called_from_bangalore_set = []


def add_area_code(phone_number, pattern):
    search_result = re.search(pattern, phone_number)

    if search_result:
        area_code = search_result.group(1)

        if area_code not in codes_called_from_bangalore_set:
            codes_called_from_bangalore_set.append(area_code)


def get_called_area_codes_from_bangalore():
    for call in calls:
        incoming_number = call[0]
        receiving_number = call[1]

        if re.match(bangalore_fixed_area_code_pattern, incoming_number):
            code_prefix_pattern = None

            if re.match(fixed_line_number_pattern, receiving_number):
                code_prefix_pattern = fixed_line_area_code_pattern
            elif re.match(mobile_line_number_pattern, receiving_number):
                code_prefix_pattern = mobile_line_area_code_pattern
            elif re.match(telemarketing_line_number_pattern, receiving_number):
                code_prefix_pattern = telemarketing_line_area_code_pattern

            if code_prefix_pattern:
                add_area_code(receiving_number, code_prefix_pattern)

    sorted_codes_called_from_bangalore_set = sorted(codes_called_from_bangalore_set)

    print("The numbers called by people in Bangalore have codes:", *sorted_codes_called_from_bangalore_set, sep="\n")


def get_bangalore_local_calls_percentage():
    total_calls = 0
    total_local_calls = 0

    for call in calls:
        incoming_number = call[0]
        receiving_number = call[1]

        if re.match(bangalore_fixed_area_code_pattern, incoming_number):
            total_calls += 1

        if re.match(bangalore_fixed_area_code_pattern, incoming_number) \
                and re.match(bangalore_fixed_area_code_pattern, receiving_number):
            total_local_calls += 1

    percentage = (total_local_calls * 100) / total_calls
    percentage = round(percentage, 2)

    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


get_called_area_codes_from_bangalore()
get_bangalore_local_calls_percentage()
