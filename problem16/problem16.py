n = 2**1000

def digitsum(n):
    n = str(n)
    s = 0
    for i in range(0, len(n)):
        s += int(n[i])
    return s

print(n)
print(digitsum(n))