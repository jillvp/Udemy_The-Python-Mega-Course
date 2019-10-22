# Coding Exercise 35: Loop Over Dictionary and Replace (E)

# Loop over the phone_numbers values and in each loop print out the phone number, but with '00' instad of '+'.

phone_numbers = {"Homer Simpson": "+324567890", "Marge Simpon": "+324678901", "Lisa Simpon": "+324789012", "Bart Simpon": "+324890123"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))
