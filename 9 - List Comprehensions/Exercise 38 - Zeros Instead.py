# Exercise 38: Zeros Instead (E)

# Define a function that takes as parameter a list that contains both numbers and strings and returns the same list but with zeros 
# instead of strings.

# For example: If your function is called with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 0, 95, 94, 0]

def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]
