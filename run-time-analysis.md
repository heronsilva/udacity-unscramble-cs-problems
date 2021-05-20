# Investigating Texts and Calls
## Task: Calculate Big O - Analysis

## Some notes

I tried not to use data structures other than lists (_e.g._, sets), as I presume we will dive in data structures in the next chapters.
However, in task #2, I couldn't think of another structure to use other than dictionaries.

I tried to solve some tasks by creating a "set", to store unique values. I might refer to them as `some_set` in the code, 
and as _unique lists_ in the description.

### Analysis result

This is how I've defined my analysis results: _raw big-o calculation of the described steps_ -> _simplified big-o notation_.

### Task 0:

Steps:
- access the first and last positions of the texts and calls lists, respectively: O(1).
- regardless of the input size, the operation will always require the same execution time, 
  as it will simply access a specific list position.

Complexity: Constant.

Worst case analysis: O(1).


### Task 1:

Steps:
- iterate over both lists: O(2n)
  - search the _unique list_ for both incoming and receiving numbers: O(2n)
    - add the new number to the _unique list_: O(1)
- get the _unique_list_ size: O(1)

Complexity: Linear.

Worst case analysis: O(2n * (2n * 1)) -> O(n).


### Task 2:

Steps:
- iterate over the calls list: O(n)
  - for both numbers, check if it's already set as a key: O(2n)
    - add or update the current phone time: O(n)
- iterate over the dictionary keys (phone numbers): O(n)
  - compare the current call time with the current longest time: O(1)
    - update the current value of the `longest_time_phone_number` dictionary: O(n)
  
Complexity: Linear.

Worst case analysis: O((n * (2n * 1n)) + (n * (1 * n))) -> O(n)

### Task 3:

#### Part A

Steps:
- iterate over the calls list: O(n)
  - check if the current call was performed from Bangalore: O(1)
  - check if the receiving number's area code or prefix matches one of the three patterns specified: O(3)
  - extract the code/prefix from the phone number: O(1)
  - search our area codes _unique list_ for the current code/prefix: O(n)
    - add the new code/prefix to the _unique_list_: O(1)
- sort the area codes list: O(n log n)

Complexity: Quasilinear.

Worst case analysis: O(n * (1 + 3 + 1 + (n * 1)) + n log n) -> O(n log n)

#### Part B

Steps:
- iterate over the calls list: O(n)
  - check if it's a call from Bangalore, one regex: O(1)
  - check if it's also a local call, two regexes: O(2)
- calculate the total local calls percentage: O(1)

Complexity: Linear.

Worst case analysis: O((n * (1 + 2)) + 1) -> O(n)

### Task 4:

Steps:
- iterate over both lists: O(2n)
  - separate incoming and receiving numbers, for both calls and texts: O(4)
  - check if the call incoming number matches the telemarketing line number pattern: O(1)
- iterate over the calling incoming numbers list: O(n)
  - check if the phone number is present on the other lists (three searches): O(3n)
  - search the _unique list_ to avoid duplicates: O(n)
    - add the new phone number: O(1)
- sort the possible telemarketers list: O(n log n) 

Complexity: Quasilinear.

Worst case analysis: O((2n * (4 + 1)) + (((n * 3) + (n * 1)) + n log n)) -> O(n log n)


## References:

- https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
- https://wiki.python.org/moin/TimeComplexity
- https://www.bigocheatsheet.com/
