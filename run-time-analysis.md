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
- iterate over both lists: O(n)
  - search the _unique list_ for both incoming and receiving numbers: O(n)
    - add the new number to the _unique list_: O(1)
- get the _unique_list_ size: O(1)

Complexity: Quadratic.

Worst case analysis: O((n^2 + 1) * 2) -> O(n^2).


### Task 2:

Steps:
- iterate over the calls list: O(n)
  - for both numbers, check if it's already set as a key: O(2)
    - add or update the current phone time: O(1)
- get the max value of the phone numbers in the dictionary: O(n)

Complexity: Linear.

Worst case analysis: O(n + 2 +1 + n) -> O(2n + 3) -> O(n)

### Task 3:

#### Part A

Steps:
- iterate over the calls list: O(n)
  - check if the current call was performed from Bangalore: O(1)
  - check if the receiving number's area code or prefix matches one of the three patterns specified: O(3)
  - extract the code/prefix from the phone number: O(1)
  - search the area codes list for the current code/prefix: O(n)
    - add the new code/prefix to the _unique_list_: O(1)
- sort the area codes list: O(n log n)

Complexity: Linear.

Worst case analysis: O((n * (5 + n)) + n log n) -> O(n^2 + n log n) -> O(n^2)

#### Part B

Steps:
- iterate over the calls list: O(n)
  - check if it's a call from Bangalore, one regex: O(1)
  - check if it's also a local call, two regexes: O(2)
- calculate the total local calls percentage: O(1)

Complexity: Linear.

Worst case analysis: O((n * 3) + 1) -> O(n)

### Task 4:

Steps:
- iterate over both lists: O(n)
  - check if the call incoming number exists in the callers list: O(n)
  - separate incoming and receiving numbers, for both calls and texts: O(4)
- iterate over the callers list: O(n)
  - check if the phone number is present on the other lists (three searches): O(3n)
    - remove the existing phone number: O(1)
- sort the possible telemarketers list: O(n log n) 

Complexity: Quadratic.

Worst case analysis: O((n^2 + 4) + (n^2 * 3 + 1) + n log n) -> O(n^2)


## References:

- https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
- https://wiki.python.org/moin/TimeComplexity
- https://www.bigocheatsheet.com/
