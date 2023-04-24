Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= (c[i] - i)
        ans %= (10**9 + 7)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= (C[i] - i)
        ans %= (10**9 + 7)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= 1000000007
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= max(0, C[i] - i)
        ans %= 1000000007
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(c[i]-i, 0)
        ans %= 1000000007
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    C = list(map(int,input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= (C[i] - i)
        ans %= 1000000007
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= 1000000007
    print(ans)

solve()

=======
Suggestion 8

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    result = 1
    for i in range(n):
        result = result * (c[i] - i) % (10**9 + 7)
    print(result)
