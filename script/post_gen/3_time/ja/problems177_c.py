Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += A[i] * A[j]
    print(ans % (10**9+7))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += A[i]*A[j]
    print(ans%(10**9+7))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        ans += A[i] * (sum(A[i+1:]) % (10**9+7))
        ans %= (10**9+7)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += A[i] * (A[i+1] - A[i]) * (N-i-1)
        ans %= 1000000007
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(N-1):
        ans += A[i] * sum(A[i+1:]) % mod
        ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += A[i] * (N - i - 1)
    print(total % (10 ** 9 + 7))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 10**9+7

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += A[i] * A[j]

    print(ans % P)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(N-1):
        ans += (A[i] * A[i+1]) * (N-1-i)
    print(ans % 1000000007)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9+7
    # Aの累積和
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    ans = 0
    for i in range(1,N):
        ans += A[i] * (S[-1] - S[i])
        ans %= mod
    print(ans)

=======
Suggestion 10

def main():
    # 配列の長さ
    N = int(input())
    # 配列を取得
    A = list(map(int, input().split()))
    # 答え
    ans = 0
    # 1個目の配列の要素を取得
    for i in range(N):
        # 2個目の配列の要素を取得
        for j in range(i + 1, N):
            # 答えに配列の要素を掛けたものを足す
            ans += A[i] * A[j]
    # 答えを出力
    print(ans % (10 ** 9 + 7))
