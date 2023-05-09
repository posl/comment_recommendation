def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))
X = int(input())
while not is_prime(X):
    X += 1
print(X)
I'm not sure if this is the best solution, but it's pretty fast.
import sys
import math
