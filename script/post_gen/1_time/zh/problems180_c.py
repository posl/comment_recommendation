Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i != n // i:
                print(n // i)
        i += 1

=======
Suggestion 2

def get_divisors(n):
    # 約数のリストを返す
    # O(√n)
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

n = int(input())
divisors = get_divisors(n)
for d in divisors:
    print(d)

=======
Suggestion 3

def main():
    N = int(input())
    ans = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
        i += 1
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 4

def main():
    import sys
    from math import sqrt
    N = int(sys.stdin.readline())
    ans = []
    for i in range(1, int(sqrt(N))+1):
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 5

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

N = int(input())
divisors = get_divisors(N)
for d in divisors:
    print(d)

=======
Suggestion 6

def find_divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            print(i)
            if i != n//i:
                print(n//i)
    return

=======
Suggestion 8

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
Suggestion 9

def divisors(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            if i != n // i:
                table.append(n // i)
        i += 1
    return table

n = int(input())
print(*sorted(divisors(n)), sep='\n')
