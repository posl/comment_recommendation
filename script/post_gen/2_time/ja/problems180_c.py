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
    return table

n = int(input())
table = divisor(n)
table.sort()
for i in range(len(table)):
    print(table[i])

=======
Suggestion 2

def divisors(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            if i != n // i:
                table.append(n//i)
        i += 1
    return table

n = int(input())
ans = divisors(n)
ans.sort()
for i in ans:
    print(i)

=======
Suggestion 3

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if i != N // i:
                print(N // i)
        i += 1

=======
Suggestion 4

def main():
    N = int(input())
    i = 1
    ans = []
    while i * i <= N:
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
        i += 1
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 5

def main():
    n = int(input())
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(i)
            ans.append(n//i)
    ans = sorted(list(set(ans)))
    for i in ans:
        print(i)

=======
Suggestion 6

def divisors(n):
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n//i)
        i += 1
    return res

n = int(input())
ans = divisors(n)
ans.sort()
for i in range(len(ans)):
    print(ans[i])

=======
Suggestion 7

def solve(n):
    res = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return sorted(res)

=======
Suggestion 8

def get_divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            if i != n // i:
                table.append(n // i)
        i += 1
    table.sort()
    return table

n = int(input())
div = get_divisor(n)
for i in div:
    print(i)

=======
Suggestion 9

def main():
    N = int(input())
    ans = []
    i = 1
    while i**2 <= N:
        if N % i == 0:
            ans.append(i)
            if i**2 != N:
                ans.append(N//i)
        i += 1
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 10

def get_divisor(n):
    divisor = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisor.append(i)
            if n//i != i:
                divisor.append(n//i)

    divisor.sort()
    return divisor

n = int(input())
divisor = get_divisor(n)
for i in range(len(divisor)):
    print(divisor[i])
