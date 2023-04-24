Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    print((pow(10,N,1000000007)-pow(9,N,1000000007)-pow(9,N,1000000007)+pow(8,N,1000000007))%1000000007)

=======
Suggestion 2

def main():
    N = int(input())
    print((pow(10, N, 10 ** 9 + 7) - pow(9, N, 10 ** 9 + 7) - pow(9, N, 10 ** 9 + 7) + pow(8, N, 10 ** 9 + 7)) % (10 ** 9 + 7))

=======
Suggestion 3

def main():
    n = int(input())
    print((10 ** n - 2 * 9 ** n + 8 ** n) % (10 ** 9 + 7))

=======
Suggestion 4

def main():
    N = int(input())
    MOD = 10**9 + 7
    ans = (10**N - 2*(9**N) + 8**N) % MOD
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    print((10**N - 2*(9**N) + 8**N) % (10**9 + 7))

=======
Suggestion 6

def main():
    N = int(input())
    print((10**N - 2*9**N + 8**N)%(10**9+7))

=======
Suggestion 7

def main():
    N = int(input())
    MOD = 10**9 + 7
    print((10**N - 2 * (9**N) + 8**N) % MOD)

=======
Suggestion 8

def main():
    N = int(input())
    mod = 10**9+7
    print(2*(10**N-9**N-9**N+8**N)%mod)

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    ans += pow(10, N, 10**9+7)
    ans -= 2*pow(9, N, 10**9+7)
    ans += pow(8, N, 10**9+7)
    print(ans % (10**9+7))

=======
Suggestion 10

def main():
    N = int(input())
    print(10**N - 2 * 9**N + 8**N)
