

from operator import truediv
def isPrime(n):
    for i in range(n):
        if i == 1 or i == 0: continue
        if n % i == 0:
            return False
    return True

number = input("Is Prime")


print(isPrime(int(number)))
