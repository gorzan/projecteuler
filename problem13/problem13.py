numbers = []
with open('raw-input.txt') as file:
    for n, line in enumerate(file):
        numbers.append(int(line))

print(sum(numbers))

