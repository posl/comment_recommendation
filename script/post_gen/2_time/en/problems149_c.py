Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return not any(n % i == 0 for i in range(3, int(n**0.5)+1, 2))

=======
Suggestion 2

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))

=======
Suggestion 3

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

=======
Suggestion 4

def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

=======
Suggestion 5

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

=======
Suggestion 6

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    x += 1

=======
Suggestion 7

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

=======
Suggestion 8

def isPrime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    else:
        x += 1

=======
Suggestion 9

def is_prime(num):
    if num == 2:
        return True
    elif num < 2 or num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True

X = int(input())
while True:
    if is_prime(X):
        print(X)
        exit()
    else:
        X += 1

The idea is to use a function to check if a number is prime or not. Then, use a while loop to check if the number is prime or not. If it is not, add 1 to the number and check again. If it is, print the number and exit the program.

The function is_prime() checks if a number is prime or not. If the number is 2, return True. If the number is less than 2 or if the number is divisible by 2, return False. Otherwise, use a for loop to check if the number is divisible by any number between 3 and the square root of the number plus 1. If it is divisible by any number, return False. Otherwise, return True.

The while loop checks if the number is prime or not. If it is not, add 1 to the number and check again. If it is, print the number and exit the program.

The code above got accepted.

=======
Suggestion 10

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
