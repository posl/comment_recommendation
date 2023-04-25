Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (i * (N + 1 - i) + 1)
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += i*(N-i+1)+1
        ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (i * (N-i+1) + 1) % mod
    print(ans % mod)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (i * (N-i+1) + 1) * i // 2
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += (N-i+1)*i+1
        ans %= MOD
    print(ans)

main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    MOD = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += (i*(N-i+1)+1)
        ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        ans += (i*(n-i+1)+1)*i//2
        ans %= mod
    print(ans)

=======
Suggestion 8

def solve(N,K):
    ans = 0
    for i in range(K,N+2):
        ans += i*N-i*(i-1)//2+(i-1)*i//2+1
        ans %= 10**9+7
    return ans

=======
Suggestion 9

def main():
    #input
    N, K = map(int, input().split())
    #compute
    ans = 0
    for i in range(K, N+2):
        ans += (N+1)*i - i*(i-1)//2
    #output
    print(ans%(10**9+7))

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7

    # N+1個の整数の中からK個以上選ぶときの選ぶ整数の和の候補の数を求める
    # 1個以上選ぶときの和の候補の数は、
    # 1 + 2 + 3 + ... + N = N(N+1)/2
    # となる
    # ただし、Nが大きいときは、N(N+1)/2をMODで割った余りを計算する必要がある
    # ここで、N(N+1)/2は、N(N+1)を2で割った整数値の商と等しい
    # なぜなら、N(N+1)は偶数であるからである
    # また、N(N+1)を2で割った整数値の商は、N(N+1)/2と等しい
    # なぜなら、N(N+1)/2は整数値であるからである
    # 以上より、N(N+1)/2をMODで割った余りは、N(N+1)/2と等しい

    # 1個以上選ぶときの和の候補の数を求める
    # 1 + 2 + 3 + ... + N = N(N+1)/2
    # 1 + 2 + 3 + ... + (N+1) = (N+1)((N+1)+1)/2
    # 1 + 2 + 3 + ... + (N+1) - 1 = N(N+1)/2
    # 1 + 2 + 3 + ... + (N+1) - 1 - 2 = N(N+1)/2 - 2
    # 1 + 2 + 3 + ... + (N+1) - 1 - 2 - 3 = N
