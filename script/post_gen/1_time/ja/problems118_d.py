Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i - a >= 0 and dp[i - a] != -1:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    print(dp[N])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + a <= N:
                dp[i + a] = max(dp[i + a], dp[i] * 10 + a)
    print(dp[N])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        for a in A:
            if i + a <= N:
                dp[i + a] = max(dp[i + a], dp[i] * 10 + a)
    print(dp[N])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1]*(N+1)
    dp[0] = 0
    for i in range(N+1):
        for a in A:
            if i-a >= 0 and dp[i-a] >= 0:
                dp[i] = max(dp[i], dp[i-a]*10+a)
    print(dp[N])

=======
Suggestion 5

def main():
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    dp = [-1]*(N+1)
    dp[0] = 0
    for i in range(1,N+1):
        for j in range(M):
            if i-A[j] >= 0 and dp[i-A[j]] != -1:
                dp[i] = max(dp[i], dp[i-A[j]]*10+A[j])
    print(dp[N])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [0] * (N + 1)
    for i in range(N + 1):
        for a in A:
            if i + a <= N:
                dp[i + a] = max(dp[i + a], dp[i] * 10 + a)
    print(dp[N])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(N, M)
    #print(A)
    #print(A[0])
    #print(A[0] * 2 + A[1] * 5 + A[2] * 5 + A[3] * 4 + A[4] * 5 + A[5] * 6 + A[6] * 3 + A[7] * 7 + A[8] * 6)
    #print(A[0] * 2 + A[1] * 5 + A[2] * 5 + A[3] * 4 + A[4] * 5 + A[5] * 6 + A[6] * 3 + A[7] * 7 + A[8] * 6 + A[9] * 6)
    #print(A[0] * 2 + A[1] * 5 + A[2] * 5 + A[3] * 4 + A[4] * 5 + A[5] * 6 + A[6] * 3 + A[7] * 7 + A[8] * 6 + A[9] * 6 + A[10] * 6)
    #print(A[0] * 2 + A[1] * 5 + A[2] * 5 + A[3] * 4 + A[4] * 5 + A[5] * 6 + A[6] * 3 + A[7] * 7 + A[8] * 6 + A[9] * 6 + A[10] * 6 + A[11] * 6)
    #print(A[0] * 2 + A[1] * 5 + A[2] * 5 + A[3] * 4 + A[4] * 5 + A[5] * 6 + A[6] * 3 + A[7] * 7 + A[8] * 6 + A[9] * 6 + A[10] * 6 + A[11] * 6 + A[12

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    A = [str(i) for i in A]
    A = "".join(A)
    dp = [-float("inf")] * (N + 1)
    dp[0] = 0
    for i in range(N):
        for a in A:
            if i + len(a) <= N:
                dp[i + len(a)] = max(dp[i + len(a)], dp[i] * 10 + int(a))
    print(dp[N])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(A)
    #print(N, M)
    count = 0
    while N > 0:
        N -= A[count]
        count += 1
    print(A[count-1])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    #print("")

    # 1 から 9 までの数字のうち A_1, A_2, ..., A_M (1 ≦ A_i ≦ 9) のいずれかでなければならない。
    # 数字 1, 2, 3, 4, 5, 6, 7, 8, 9 を 1 つ作るには、それぞれちょうど 2, 5, 5, 4, 5, 6, 3, 7, 6 本のマッチ棒を使う。
    # 1 から 9 までの数字のうち A_1, A_2, ..., A_M (1 ≦ A_i ≦ 9) のいずれかでなければならない。
    # 数字 1, 2, 3, 4, 5, 6, 7, 8, 9 を 1 つ作るには、それぞれちょうど 2, 5, 5, 4, 5, 6, 3, 7, 6 本のマッチ棒を使う。
    # A_i は全て異なる。
    # ちょうど N 本のマッチ棒を使って条件を満たすように作れる整数が存在する。
    #print("A:", A)
    A.sort()
    #print("A:", A)
    #print("")
    #print("N:", N)
    #print("")

    # 1 から 9 までの数字のうち A_1, A_2, ..., A_M (1 ≦ A_i ≦ 9) のいずれかでなければならない。
    # 数字 1, 2, 3, 4, 5, 6, 7, 8, 9 を 1
