Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    mod = 10**9+7
    ans = 1
    for i in range(N):
        ans *= max(C[i]-i, 0)
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    m = 10**9 + 7
    ans = 1
    for i in range(n):
        ans *= max(0, c[i] - i)
        ans %= m
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans = ans * max(c[i] - i, 0) % (10 ** 9 + 7)
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    mod = 10**9 + 7
    ans = 1
    for i in range(N):
        ans *= max(C[i] - i, 0)
        ans %= mod
    return ans

print(solve())

=======
Suggestion 5

def main():
    n = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(n):
        ans = ans * (C[i]-i) % 1000000007
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans = ans * max(0, C[i] - i) % (10 ** 9 + 7)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    c = list(map(int, input().split()))

    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(0, c[i] - i)
        ans %= 10 ** 9 + 7

    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= 1000000007
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans = ans * max(0, C[i] - i) % (10**9 + 7)
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    c = list(map(int,input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans = ans * max(0,c[i]-i) % 1000000007
    print(ans)
