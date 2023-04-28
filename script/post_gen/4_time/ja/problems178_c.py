Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print((pow(10, n, 10**9+7) - pow(9, n, 10**9+7) - pow(9, n, 10**9+7) + pow(8, n, 10**9+7)) % (10**9+7))

=======
Suggestion 2

def main():
    n = int(input())
    mod = 10**9 + 7
    ans = pow(10,n,mod) - pow(9,n,mod) - pow(9,n,mod) + pow(8,n,mod)
    ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    print((10**N - 2*9**N + 8**N) % (10**9 + 7))

=======
Suggestion 4

def p178_c():
    n = int(input())
    ans = pow(10, n, 10**9+7) - pow(9, n, 10**9+7) - pow(9, n, 10**9+7) + pow(8, n, 10**9+7)
    print(ans % (10**9+7))

=======
Suggestion 5

def main():
    import sys
    readline = sys.stdin.readline
    mod = 10 ** 9 + 7
    N = int(readline())
    ans = pow(10, N, mod) - 2 * pow(9, N, mod) + pow(8, N, mod)
    print(ans % mod)

=======
Suggestion 6

def main():
    N = int(input())
    print((10**N - 2*(9**N) + 8**N) % (10**9 + 7))
