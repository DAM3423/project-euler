# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

limit = 1000  # Dynamic limit which can be moved whenever
divisible = []  # Array for storing all integers divisible by 3 and 5

i = 0

while i < limit:

    # Checking 3 first
    if i % 3 == 0:
        divisible.append(i)
    else:
        # Then 5
        if i % 5 == 0:
            divisible.append(i)

    i += 1


total = sum(divisible)

print(total)