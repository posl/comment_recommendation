Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for a in range(1, n):
        for b in range(1, n):
            c = n - a * b
            if c > 0:
                count += 1
            else:
                break
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    count = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            c = n - a * b
            if c > 0:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for A in range(1, N):
        for B in range(1, N):
            C = N - A * B
            if C > 0:
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        for j in range(1, n):
            if n - i * j > 0:
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j >= n:
                break
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        for j in range(1, N):
            if N - i * j > 0:
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        if i*i > N:
            break
        for j in range(1, N):
            if i*j > N:
                break
            if i*j < N:
                ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    ans = 0
    for i in range(1, N):
        for j in range(1, N):
            if i * j >= N:
                break
            if (N - i * j) % j == 0:
                ans += 1
    print(ans)

=======
Suggestion 9

def solve(n):
    res = 0
    for i in range(1, n):
        res += (n-1)//i
    return res
