Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans = ans * max(0, c[i] - i) % (10**9 + 7)
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= max(C[i] - i, 0)
        ans %= 10 ** 9 + 7
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10 ** 9 + 7

    C.sort()
    ans = 1

    for i in range(N):
        ans *= (C[i] - i)
        ans %= MOD

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= (10**9 + 7)
    print(ans)

=======
Suggestion 5

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

=======
Suggestion 6

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
Suggestion 7

def resolve():
    MOD = 10**9+7
    N = int(input())
    C = list(map(int, input().split()))

    C.sort()
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= MOD
    print(ans)

=======
Suggestion 8

def main():
    n=int(input())
    c=list(map(int,input().split()))
    mod=10**9+7
    c.sort()
    ans=1
    for i in range(n):
        ans*=(c[i]-i)
        ans%=mod
    print(ans)

main()

=======
Suggestion 9

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
Suggestion 10

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= 1000000007
    print(ans)
