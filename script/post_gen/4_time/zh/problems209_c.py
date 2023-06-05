Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= (c[i] - i)
        ans %= (10 ** 9 + 7)
    print(ans)

=======
Suggestion 3

def solve(n, c):
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= 1000000007
    return ans

=======
Suggestion 4

def main():
    n = int(input())
    c = list(map(int,input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(0,c[i]-i)
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
        ans *= max(0, c[i] - i)
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 6

def main():
    n=int(input())
    c=list(map(int,input().split()))
    c.sort()
    ans=1
    for i in range(n):
        ans*=(c[i]-i)
        ans%=1000000007
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= 1000000007
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    mod = 10 ** 9 + 7

    ans = 1
    for i in range(n):
        ans *= (c[i] - i)
        ans %= mod

    print(ans)

=======
Suggestion 9

def count_seq(n, c):
    c.sort()
    count = 1
    for i in range(n):
        count *= c[i] - i
        count %= (10 ** 9 + 7)
    return count

=======
Suggestion 10

def main():
    N = int(input())
    C = list(map(int,input().split()))
    C.sort()
    mod = 10**9+7
    ans = 1
    for i in range(N):
        ans = ans * (C[i]-i) % mod
    print(ans)
