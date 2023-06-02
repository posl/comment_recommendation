Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i+j):
            print('高桥')
            exit()
print('青木')

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): # int(n**0.5)+1 为了减少循环次数
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

=======
Suggestion 3

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

A,B,C,D = map(int,input().split())

=======
Suggestion 4

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

=======
Suggestion 5

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 ==0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i ==0:
            return False
    return True

a, b, c, d = map(int, input().split())

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

a,b,c,d = map(int,input().split())
for i in range(a,b+1):
    for j in range(c,d+1):
        if is_prime(i+j):
            print("高桥")
            exit()
print("青木")

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

a, b, c, d = map(int, input().split())

=======
Suggestion 8

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

=======
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

=======
Suggestion 10

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 ==0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    if is_prime(i):
        break
else:
    print('No')
    exit()

for i in range(c, d+1):
    if is_prime(i):
        break
else:
    print('No')
    exit()

print('Yes')
