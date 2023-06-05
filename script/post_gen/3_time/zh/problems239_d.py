Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    if is_prime(i+c):
        print("高桥")
        exit()

print("青木")

=======
Suggestion 2

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

=======
Suggestion 3

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

a,b,c,d = map(int,input().split())
for i in range(a,b+1):
    if is_prime(i):
        for j in range(c,d+1):
            if is_prime(j):
                if i+j == 2:
                    print("High")
                    exit()
                elif i+j == 3:
                    print("High")
                    exit()
                elif i+j == 5:
                    print("High")
                    exit()
                elif i+j == 7:
                    print("High")
                    exit()
                elif i+j == 11:
                    print("High")
                    exit()
                elif i+j == 13:
                    print("High")
                    exit()
                else:
                    print("Low")
                    exit()

=======
Suggestion 4

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n//2+1):
            if n % i == 0:
                return False
        return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    if is_prime(i):
        for j in range(c, d+1):
            if is_prime(j):
                if i + j == 2:
                    print("High")
                    exit()
                elif (i + j) % 2 == 0:
                    print("High")
                    exit()
                else:
                    print("Low")
                    exit()
print("Low")

=======
Suggestion 5

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

a, b, c, d = map(int, input().split())

=======
Suggestion 6

def isPrime(num):
    if num==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

a,b,c,d=map(int,input().split())

=======
Suggestion 7

def check_prime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

=======
Suggestion 8

def isPrime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                return False
        return True

=======
Suggestion 9

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

a, b, c, d = map(int, input().split())
g = 0
for i in range(a, b + 1):
    if is_prime(i):
        g = i
        break
for i in range(c, d + 1):
    if is_prime(i):
        if i - g > 0:
            print("青木")
        else:
            print("高桥")
        break

=======
Suggestion 10

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    for j in range(c, d+1):
        if isPrime(i+j):
            print("青木")
            exit()
print("高桥")
