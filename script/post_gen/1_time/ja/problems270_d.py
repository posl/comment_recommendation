Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N + 1):
        for j in range(K):
            if i - A[j] >= 0:
                dp[i] |= not dp[i - A[j]]
            else:
                break
    if dp[N]:
        print("First")
    else:
        print("Second")

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (n + 1)
    for i in range(1, n + 1):
        for j in range(k):
            if i - a[j] >= 0:
                dp[i] |= not dp[i - a[j]]
    print("Takahashi" if dp[n] else "Aoki")

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(k):
            if i-a[j] < 0:
                break
            if dp[i-a[j]] == 0:
                dp[i] = 1
    if dp[n] == 0:
        print("Second")
    else:
        print("First")

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K):
            if i - A[j] < 0:
                break
            if dp[i - A[j]] == 0:
                dp[i] = 1
                break
    if dp[N] == 1:
        print("Takahashi")
    else:
        print("Aoki")
solve()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    dp[0] = 0
    for i in range(N):
        for j in range(K):
            if i - A[j] >= 0:
                dp[i] = max(dp[i], dp[i - A[j]] + 1)
    print(dp[N])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = A[::-1]
    for a in A:
        if N%a == 0:
            print(N - a)
            return

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #初期化
    dp = [0] * (N+1)
    dp[1] = 1
    #dp[i] = iを取るときの勝ち負け
    #dp[i] = 0:負け
    #dp[i] = 1:勝ち
    for i in range(2,N+1):
        for j in range(K):
            if A[j] > i:
                break
            if dp[i-A[j]] == 0:
                dp[i] = 1
                break
    if dp[N] == 1:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)
    #print(N,K)
    if A[0] == 1:
        print(N-1)
        return
    if N == 1:
        print(0)
        return
    for i in range(K):
        if N % A[i] == 0:
            print(N-A[i])
            return
    for i in range(K):
        if N % A[i] == 1:
            print(N-A[i]-1)
            return
    for i in range(K):
        if N % A[i] > 1:
            print(N%A[i])
            return

=======
Suggestion 9

def main():
    #入力
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    #最初の山の石の数を変数に代入
    stone = n
    #高橋君が取り除く石の数を変数に代入
    takahashi = 0
    #青木君が取り除く石の数を変数に代入
    aoki = 0
    #高橋君が取り除く石の数を増やす
    for i in range(k):
        takahashi += a[i]
        #青木君が取り除く石の数を増やす
        for j in range(i,k):
            aoki += a[j]
            #高橋君が取り除く石の数が青木君が取り除く石の数より大きい場合
            if takahashi > aoki:
                #青木君が取り除く石の数を増やす
                aoki += a[j]
            #高橋君が取り除く石の数が青木君が取り除く石の数より小さい場合
            elif takahashi < aoki:
                #高橋君が取り除く石の数を増やす
                takahashi += a[i]
            #高橋君が取り除く石の数が青木君が取り除く石の数と同じ場合
            else:
                #青木君が取り除く石の数を増やす
                aoki += a[j]
    #高橋君が取り除く石の数を出力
    print(takahashi)

=======
Suggestion 10

def get_min(n, a):
    if n in a:
        return n
    else:
        for i in a:
            if n % i == 0:
                return i
        for i in a:
            if n % i == 1:
                return i
        for i in a:
            if n % i == 2:
                return i
        for i in a:
            if n % i == 3:
                return i
        for i in a:
            if n % i == 4:
                return i
        for i in a:
            if n % i == 5:
                return i
        for i in a:
            if n % i == 6:
                return i
        for i in a:
            if n % i == 7:
                return i
        for i in a:
            if n % i == 8:
                return i
        for i in a:
            if n % i == 9:
                return i

n, k = map(int, input().split())
a = list(map(int, input().split()))

while True:
    m = get_min(n, a)
    n -= m
    if n == 0:
        print(m)
        break
