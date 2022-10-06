from sys import argv


def is_prime(a):
    check = True
    for i in range(2, a):
        if a % i == 0:
            check = False
    return check


a = int(argv[1])
res = 0

for b in range(2, a):
    if is_prime(b):
        res = res + b
print(sum)
