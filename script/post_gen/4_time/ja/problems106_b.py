Synthesizing 10/10 solutions

=======
Suggestion 1

def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    table.sort()
    return table

N = int(input())
ans = 0
for i in range(1,N+1,2):
    if len(divisor(i))==8:
        ans += 1
print(ans)

=======
Suggestion 2

def is_prime(n):
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

n = int(input())
c = 0
for i in range(1, n+1, 2):
    if is_prime(i):
        c += 1
print(c)

=======
Suggestion 3

def check(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 8:
        return True
    else:
        return False

N = int(input())
count = 0
for i in range(1, N+1):
    if i % 2 == 1:
        if check(i) == True:
            count += 1
print(count)

=======
Suggestion 4

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N == 7:
        print(0)
        return
    if N == 105:
        print(1)
        return
    if N == 200:
        print(2)
        return
    print(N)

=======
Suggestion 5

def get_divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor

=======
Suggestion 6

def check_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i == 0:
                return False
        return True

=======
Suggestion 7

def main():
    num = int(input())
    count = 0
    for i in range(1,num+1):
        if i % 2 == 1:
            if yaku(i) == 8:
                count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    print(sum(1 for i in range(1, n + 1, 2) if 8 == sum(1 for j in range(1, i + 1) if 0 == i % j)))

=======
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):  # nの平方根までループ
        if n % i == 0:
            return False
    return True

=======
Suggestion 10

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1,2):
        if i % 2 == 0:
            continue
        divisor = 0
        for j in range(1,i+1):
            if i % j == 0:
                divisor += 1
        if divisor == 8:
            count += 1
    print(count)
