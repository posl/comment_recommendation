Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    ans = 0
    while n > 0:
        ans += 1
        n //= 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(2, n+1):
        if i*i <= n:
            ans += n//i - 1
        else:
            ans += n//i
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
            ans += 1
        else:
            n -= 1
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    while n > 1:
        ans += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            ans = i
        i += 1
    ans += N // ans - 2
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    x = 1
    y = 1
    ans = 0
    while x * y < n:
        if x == y:
            x += 1
        elif x < y:
            x += 1
        else:
            y += 1
        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1,N):
        if i * i > N:
            break
        if N % i == 0:
            ans = i
    print(ans + N // ans - 2)

=======
Suggestion 9

def solve():
    N = int(input())
    ans = 0
    for i in range(1, 1000000):
        if i * i > N:
            break
        ans = i
    print(ans * 2 - 1)
    return 0

=======
Suggestion 10

def main():
    N = int(input())
    i = 1
    j = 1
    count = 0
    while True:
        if N <= i*j:
            break
        if i == j:
            j += 1
            count += 1
        else:
            i += 1
            count += 1
    print(count)
