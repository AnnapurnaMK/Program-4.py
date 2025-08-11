# Program-4.py

Problem 4: Count Multiples in List

## Problem Statement

Given a list of integers, count how many numbers are divisible by each of the integers from **1 to 9**, and return the results as a dictionary.

# Language Used
Python 3.x

Built-in data structures (lists, dictionaries)

Type hints (List[int], Dict[int, int])

List comprehension for concise logic

## Input

- A list of integers  
  Example:  
  `[1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]`


## Output

- A dictionary where:
  - Keys are numbers from `1` to `9`
  - Values are counts of how many numbers in the list are divisible by each key

# Features
Efficient counting using list and dictionary comprehensions

Supports any integer list size

Pure Python – no external libraries required

Modular and testable design

Readable and concise code with type annotations

calable to large input lists

# Example Run
Input:
[1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
Output:
{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

# Logic Overview
For every number i from 1 to 9:

Count how many numbers in the list are divisible by i

Store the result in a dictionary

