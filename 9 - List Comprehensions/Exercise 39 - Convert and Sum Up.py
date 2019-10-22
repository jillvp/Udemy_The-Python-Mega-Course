# Exercise 39: Convert and Sum Up (E)

# Define a function that takes as parameter a list that contains decimal numbers as strings and returns the sum of those numbers.
# For example: If your function is called with foo(['1.2', '2.6', '3.3']) it should return 7.1.

def foo(lst):
    return sum([float(i) for i in lst])
