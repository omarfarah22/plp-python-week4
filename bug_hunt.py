count = 1
total = 0

# BUG: The while statement was missing a colon.
# BUG: The condition was < 5, which excluded 5, so I changed it to <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: I changed + to a comma because total is an integer.
print("Sum of 1 to 5 is:", total)