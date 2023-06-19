Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for x in range(3, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

=======
Suggestion 2

def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        else:
            return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    if is_prime(i):
        for j in range(c, d+1):
            if is_prime(j):
                print('Y')
                break
        else:
            print('N')
        break
else:
    print('N')

=======
Suggestion 3

def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    return True

=======
Suggestion 5

def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i+j):
            print("高桥")
            exit()
else:
    print("青木")

=======
Suggestion 6

def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False

    return True

=======
Suggestion 7

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

=======
Suggestion 8

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): # 从2开始到n的平方根+1
        if n % i == 0:
            return False
    return True

=======
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
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
Suggestion 10

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1,2))

a,b,c,d = map(int,input().split())
