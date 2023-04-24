Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 2):
        ans += (N * i - i * (i - 1) // 2) - (i * (i - 1) // 2) + 1
        ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (N-i+1)*i + 1
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (i * (N - i + 1) + 1) * i // 2
        ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (i*(N-i+1)+1)
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (N - i + 1) * i + 1
        ans %= MOD
    print(ans)

=======
Suggestion 6

def main():

    # input
    N, K = map(int, input().split())

    # compute
    ans = 0
    for i in range(K, N+2):
        ans += i*(N-i+1)+1
        ans %= 10**9+7

    # output
    print(ans)

=======
Suggestion 7

def solve(N, K):
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += (N+1)*N//2 - (N-i+1)*i//2 + 1
        ans %= mod
    return ans

=======
Suggestion 8

def main():
    # 入力
    N, K = map(int, input().split())
    
    # 10^9+7
    mod = 10**9+7
    
    # 答え
    ans = 0
    
    # 答えを求める
    for i in range(K, N+2):
        # 1~iの総和
        sum1 = i*(i+1)//2
        # N~N-i+1の総和
        sum2 = (N-i+1)*N//2 + (N-i+1)
        # 答えに加算
        ans = (ans + sum1 - sum2 + 1) % mod
    
    # 出力
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7

    # 累積和を作る
    sum_list = [0]
    for i in range(1, N + 2):
        sum_list.append(sum_list[i - 1] + i)

    # 答えを求める
    ans = 0
    for i in range(K, N + 2):
        ans += sum_list[i] - sum_list[i - K] + 1
        ans %= MOD

    print(ans)

=======
Suggestion 10

def calc(n, k):
    if k == 1:
        return n
    else:
        return (n-k+1)*calc(n, k-1) % (10**9+7)
