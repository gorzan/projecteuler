def collatz_rule(n):
    if n % 2 == 0:
        return n/2
    else:
        return (3*n) + 1


def chain(number, steps=0):
    if number == 1:
        return steps
    else:
        return chain(collatz_rule(number), steps+1)


longest_number = 0
longest_length = 0

for number in range(1, 1000000):
    length = chain(number)
    if length > longest_length:
        longest_length = length
        longest_number = number

print("Longest length: " + str(longest_length))
print("Number with longest length: " + str(longest_number))