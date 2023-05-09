Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    mod = 10**9 + 7
    ans = pow(10,n,mod) - 2*pow(9,n,mod) + pow(8,n,mod)
    ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    print((10**n - 2 * 9**n + 8**n) % (10**9 + 7))

=======
Suggestion 3

def main():
    n = int(input())
    mod = 10**9 + 7
    print((10**n - 2*9**n + 8**n)%mod)

=======
Suggestion 4

def main():
    n = int(input())
    print(10**n - 2*9**n + 8**n)

=======
Suggestion 5

def solve(n):
    MOD = 10**9 + 7
    return (10**n - 2*9**n + 8**n) % MOD

print(solve(int(input())))

=======
Suggestion 6

def solve():
    N = int(input())
    ans = (10**N - 2*(9**N) + 8**N) % (10**9 + 7)
    print(ans)
    return 0

=======
Suggestion 7

def main():
    n = int(input())
    #print(n)
    mod = 10**9 + 7
    #print(mod)
    ans = pow(10,n,mod) - 2*pow(9,n,mod) + pow(8,n,mod)
    #print(ans)
    print(ans%mod)

=======
Suggestion 8

def solve(n):
    # 0 がある
    # 9 がある
    # 0 と 9 がある
    # 0 と 9 がない
    # 0 がな
