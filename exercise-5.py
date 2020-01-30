# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it 
n_terms = int(input(f'Calculate and print the first 50 terms of the fibonacci sequence.'))
n1, n2 = 0, 1
count = 0

if n_terms > 0:
    print("Positive integer")
elif n_terms == 1:
    print(f"Fibonacci sequence upto, {n_terms}:")
    print(n1)
else:
    print("Fibonacci sequence:")
while count < n_terms:
    print(n1)
    sum_nth = n1 + n2
    n1 = n2
    n2 = sum_nth
    count += 1
