Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    C = list(map(int, input().split()))
    A = [0] * N
    A[0] = 1
    for i in range(1, N):
        if C[i-1] < C[i]:
            A[i] = A[i-1] + 1
        else:
            A[i] = 1
    print(A)
    ans = 1
    for i in range(N):
        ans *= A[i] ** A[i]
    print(ans % (10**9 + 7))

main()

=======
Suggestion 2

def main():
    N = int(input())
    C = list(map(int, input().split()))
    if N == 2:
        if C[0] == C[1]:
            print(2)
        else:
            print(1)
        return

    # 1番目の要素は必ず1
    A = [1]
    # 1番目の要素を決めたので、2番目以降の要素を決める
    for i in range(1, N):
        # 1番目の要素が決まっているので、2番目以降の要素は1番目の要素より小さくならない
        if A[i-1] > C[i]:
            print(0)
            return
        # 1番目の要素が決まっているので、2番目以降の要素は1番目の要素と同じにならない
        if A[i-1] == C[i]:
            A.append(A[i-1])
        else:
            A.append(A[i-1]+1)
    print(A[-1])

=======
Suggestion 3

def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 1
    for i in range(N):
        if i == 0:
            ans *= C[i]
        else:
            ans *= max(0, C[i] - C[i - 1] + 1)
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    MOD = 10**9+7
    ans = 1
    for i in range(N):
        ans *= C[i]-i
        ans %= MOD
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    C = [int(x) for x in input().split()]
    mod = 10 ** 9 + 7
    ans = 1
    for i in range(N):
        if i == 0:
            ans *= C[i]
            continue
        if C[i] < C[i-1]:
            print(0)
            return
        elif C[i] == C[i-1]:
            ans *= C[i] - 1
        else:
            ans *= C[i] - i
        ans %= mod
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    if C[0] == C[-1]:
        print(0)
        return
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= 10**9 + 7
    print(ans)

main()

=======
Suggestion 8

def main():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10 ** 9 + 7

    # 1 <= Ai <= Ci (1 <= i <= N)
    # Ai != Aj (1 <= i < j <= N)

    # Ai = 1 のとき、Ai+1 = 1 となる Ci が存在するか
    # Ai = 2 のとき、Ai+1 = 2 となる Ci が存在するか
    # Ai = 3 のとき、Ai+1 = 3 となる Ci が存在するか
    # Ai = 4 のとき、Ai+1 = 4 となる Ci が存在するか
    # Ai = 5 のとき、Ai+1 = 5 となる Ci が存在するか
    # Ai = 6 のとき、Ai+1 = 6 となる Ci が存在するか
    # Ai = 7 のとき、Ai+1 = 7 となる Ci が存在するか
    # Ai = 8 のとき、Ai+1 = 8 となる Ci が存在するか
    # Ai = 9 のとき、Ai+1 = 9 となる Ci が存在するか
    # Ai = 10 のとき、Ai+1 = 10 となる Ci が存在するか

    # Ai = 1 のとき、Ai+1 = 1 となる Ci は 1 つ
    # Ai = 2 のとき、Ai+1 = 2 となる Ci は 2 つ
    # Ai = 3 のとき、Ai+1 = 3 となる Ci は 3 つ
    # Ai = 4 のとき、Ai+1 = 4 となる Ci は 4 つ
    # Ai = 5 のとき、Ai+1 = 5 となる Ci は 5 つ
    # Ai = 6 のとき、Ai+1 = 6 となる Ci は 6 つ
    #

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    C = list(map(int, input().split()))

    #初期値
    ans = 1
    mod = 10**9+7

    #処理
    for i in range(N-1):
        if C[i] == C[i+1]:
            ans *= 2
            ans %= mod
        elif C[i] > C[i+1]:
            ans *= 1
            ans %= mod
        else:
            ans *= 2
            ans %= mod
            if C[i] == C[i+1]-1:
                ans *= 1
                ans %= mod
            else:
                ans *= 0
                ans %= mod

    #出力
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    c = list(map(int, input().split()))
    #print(n)
    #print(c)
    #print(len(c))
    #print(c[0])
    #print(c[-1])

    #dp = [[0] * (n+1) for i in range(n+1)]
    dp = [0] * (n+1)
    #print(dp)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % (10**9+7)
    #print(dp)

    ans = 1
    for i in range(n):
        if i == 0:
            ans *= dp[c[i]-1]
        else:
            if c[i] == c[i-1]:
                ans *= dp[c[i]-1] - dp[c[i]-2]
            else:
                ans *= dp[c[i]-1]
        ans = ans % (10**9+7)
    print(ans)
