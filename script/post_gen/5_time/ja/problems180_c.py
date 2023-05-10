Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    l = []
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            l.append(i)
            if i != N//i:
                l.append(N//i)
    l.sort()
    for i in l:
        print(i)

=======
Suggestion 2

def main():
    n = int(input())
    ans = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            ans.append(n // i)
    ans = list(set(ans))
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 3

def main():
    N = int(input())
    divisors = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N // i)
        i += 1
    divisors.sort()
    for divisor in divisors:
        print(divisor)

=======
Suggestion 4

def get_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
        i += 1
    divisors.sort()
    return divisors

n = int(input())
divisors = get_divisors(n)
for i in divisors:
    print(i)

=======
Suggestion 5

def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            divisors.append(i)
            if num//i != i:
                divisors.append(num//i)
    divisors.sort()
    return divisors

N = int(input())
divisors = get_divisors(N)
for d in divisors:
    print(d)

=======
Suggestion 6

def main():
    N = int(input())
    ans = set()
    i = 1
    while i * i <= N:
        if N % i == 0:
            ans.add(i)
            ans.add(N // i)
        i += 1
    for a in sorted(ans):
        print(a)

=======
Suggestion 7

def solve():
    N = int(input())
    ans = set()
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans.add(i)
            ans.add(N // i)
    for a in sorted(ans):
        print(a)

=======
Suggestion 8

def main():
    n = int(input())
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            ans.append(N//i)
    ans = sorted(list(set(ans)))
    print(*ans, sep='\n')

=======
Suggestion 10

def main():
    n = int(input())
    ans = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])
