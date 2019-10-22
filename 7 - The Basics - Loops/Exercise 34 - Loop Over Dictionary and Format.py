# Coding Exercise 34: Loop Over Dictionary and Format (E)

# Write a program that loops over a Dictionary.
# The code should loop over the dictionary items and in each iteration should print out the dictionary key, a colon, a space, and the corresponding value.

phone_numbers = {"Homer Simpson": "+324567890", "Marge Simpon": "+324678901", "Lisa Simpon": "+324789012", "Bart Simpon": "+324890123"}

for key, value in phone_numbers.items():
    print("{}: {}".format(key, value))
