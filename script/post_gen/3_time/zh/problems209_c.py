Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    mod = 10 ** 9 + 7
    ans = 1
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans = (ans * (c[i] - i)) % (10 ** 9 + 7)
    print(ans)

=======
Suggestion 3

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
Suggestion 4

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(0, c[i] - i)
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
        ans *= (c[i] - i)
        ans %= (10**9 + 7)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    MOD = 10**9 + 7
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= MOD
    print(ans)

main()

=======
Suggestion 7

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= (C[i] - i)
        ans %= 1000000007
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    MOD = 10**9 + 7
    ans = 1
    for i in range(N):
        ans *= max(0, C[i] - i)
        ans %= MOD
    print(ans)

solve()

=======
Suggestion 9

def main():
    n = int(input())
    c = list(map(int, input().split()))
    mod = 10**9+7
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i]-i
        ans %= mod
    print(ans)
