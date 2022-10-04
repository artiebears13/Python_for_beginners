from sys import argv


def IsPrime(a):
    isprime=True
    for i in range(2,a):
        if a%i==0:
            isprime=False
    return isprime

a=int(argv[1])
sum=0

for b in range(2,a):
    if IsPrime(b)==True:
        sum=sum+b
print(sum)
