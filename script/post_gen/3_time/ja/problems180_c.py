Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = set()
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans.add(i)
            ans.add(N//i)
    ans = sorted(list(ans))
    print(*ans, sep="\n")

=======
Suggestion 2

def solve(n):
    ans = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
        i += 1
    ans.sort()
    return ans

=======
Suggestion 3

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
Suggestion 4

def main():
    n = int(input())
    i = 1
    ans = []
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
        i += 1
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 5

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return sorted(divisors)

N = int(input())
ans = divisors(N)
for i in range(len(ans)):
    print(ans[i])

=======
Suggestion 6

def solve():
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
    for a in ans:
        print(a)

=======
Suggestion 7

def main():
    n = int(input())
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
    ans.sort()
    print(*ans, sep='\n')

=======
Suggestion 8

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            if i != N//i:
                ans.append(N//i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    n = int(input())
    l = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            l.append(i)
            if i != n // i:
                l.append(n // i)
    l.sort()
    for i in l:
        print(i)

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    i = 1
    ans = []
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            ans.append(n // i)
        i += 1
    ans = sorted(list(set(ans)))
    print(*ans, sep='\n')
