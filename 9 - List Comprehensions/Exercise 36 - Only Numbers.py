# Exercise 36: Only Numbers (E) 

# Define a function that takes as parameter a list that contains both numbers and strings and returns the list containing only the numbers.
# For example: If your function is called with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 95, 94].

def foo(lst):
    return [i for i in lst if not isinstance(i, str)]
