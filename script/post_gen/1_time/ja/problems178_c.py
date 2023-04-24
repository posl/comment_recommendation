Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    print((pow(10,N,10**9+7)-2*pow(9,N,10**9+7)+pow(8,N,10**9+7))%(10**9+7))

=======
Suggestion 2

def main():
    mod = 10 ** 9 + 7
    N = int(input())
    print((10 ** N - 2 * 9 ** N + 8 ** N) % mod)

=======
Suggestion 3

def main():
    n = int(input())
    mod = 10**9 + 7
    print((10**n - 2*(9**n) + 8**n) % mod)

=======
Suggestion 4

def main():
    N = int(input())
    print((10**N - 2*(9**N) + 8**N)%(10**9+7))

=======
Suggestion 5

def main():
    n = int(input())
    print((10**n - 2*(9**n) + 8**n) % (10**9+7))

=======
Suggestion 6

def main():
    N = int(input())
    mod = 10**9+7
    print((10**N-2*(9**N)+8**N)%mod)

=======
Suggestion 7

def main():
    n = int(input())
    print((9 ** n + 9 ** n - 8 ** n) % (10 ** 9 + 7))

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    mod = 10**9+7
    for i in range(1,n+1):
        ans = (ans + (pow(10,i,mod)-pow(9,i,mod)-pow(9,i,mod)+pow(8,i,mod))%mod)%mod
    print(ans)

=======
Suggestion 9

def solve(n):
    return 10**n - 2*(9**n) + 8**n

=======
Suggestion 10

def main():
    N = int(input())
    print((N-2)*9)
