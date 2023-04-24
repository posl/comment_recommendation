Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count("1") == K:
            S.add(sum(A[j] for j in range(N) if (i >> j) & 1))
    for num in range((max(S) // D) * D, -1, -D):
        if num in S:
            print(num)
            return
    print(-1)

=======
Suggestion 2

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] + A[j] <= 100:
                S.add(A[i] + A[j])
    S = sorted(S, reverse=True)
    for s in S:
        if s % D == 0:
            print(s)
            exit()
    print(-1)

=======
Suggestion 3

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count('1') == K:
            s = 0
            for j in range(N):
                if (i >> j) & 1:
                    s += A[j]
            S.add(s)
    ans = max([i for i in S if i % D == 0] or [-1])
    print(ans)

=======
Suggestion 4

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, D, A)
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i]+A[j])
    #print(S)
    ans = -1
    for i in S:
        if i % D == 0:
            ans = max(ans, i)
    print(ans)

=======
Suggestion 5

def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for i in range(2**n):
        tmp = 0
        for j in range(n):
            if (i >> j) & 1:
                tmp += a[j]
        s.add(tmp)
    ans = -1
    for i in s:
        if i % d == 0:
            ans = max(ans, i)
    print(ans)

=======
Suggestion 6

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i] + A[j])
    S = list(S)
    S.sort()
    S = S[::-1]
    for i in range(len(S)):
        if S[i] % D == 0:
            print(S[i])
            exit()
    print(-1)

=======
Suggestion 7

def main():
    N, K, D = list(map(int, input().split()))
    A = list(map(int, input().split()))
    
    S = set()
    for i in range(K):
        S |= set([sum(A[j:j+i+1]) for j in range(N-i)])
    S = sorted(list(S), reverse=True)
    for s in S:
        if s % D == 0:
            print(s)
            return
    print(-1)

main()

I think this is a good problem to learn about the set data type. I think it is very useful to know about it. I also think that this problem is a good problem to learn about the sorted function. I think it is very useful to know about it.

=======
Suggestion 8

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    # ここに処理を書く
    print(max(S) if len(S) > 0 else -1)

=======
Suggestion 9

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))

    # DP[i][j] = i番目までのAの中からj個選んだ時の総和の最大値
    DP = [[0 for i in range(K + 1)] for j in range(N + 1)]
    DP[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if DP[i - 1][j - 1] == 1:
                DP[i][j] = 1
                if A[i - 1] % D == 0:
                    DP[i][j] = DP[i - 1][j] | DP[i - 1][j - 1]
                else:
                    DP[i][j] = DP[i - 1][j]

    if DP[N][K] == 0:
        print(-1)
        return

    ans = 0
    for i in range(N, 0, -1):
        if DP[i][K] == 1 and DP[i - 1][K - 1] == 0:
            ans += A[i - 1]
            K -= 1
            if K == 0:
                break

    if ans % D == 0:
        print(ans)
    else:
        print(-1)

=======
Suggestion 10

def read_int():
    return int(raw_input())
