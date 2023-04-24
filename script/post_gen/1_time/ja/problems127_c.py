Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    print(max(0, min(R) - max(L) + 1))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(M):
        l, r = map(int, input().split())
        L[l - 1] += 1
        R[r - 1] += 1
    res = 0
    for i in range(N):
        if i > 0:
            L[i] += L[i - 1]
        if L[i] == M:
            res += 1
        if R[i] > 0:
            L[i] -= R[i]
    print(res)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    L, R = [], []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    # 1枚だけで全てのゲートを通過できるIDカードの枚数を出力せよ
    print(min(R) - max(L) + 1 if min(R) - max(L) + 1 > 0 else 0)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] * (N + 1)
    for i in range(M):
        l, r = map(int, input().split())
        A[l - 1] += 1
        A[r] -= 1
    for i in range(N):
        A[i + 1] += A[i]
    print(A.count(M))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    l = [0] * (N+1)
    for _ in range(M):
        L, R = map(int, input().split())
        l[L-1] += 1
        l[R] -= 1
    print(sum([1 for i in range(N) if sum(l[:i+1]) == M]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    l = [0] * (N + 1)
    r = [0] * (N + 1)
    for _ in range(M):
        L, R = map(int, input().split())
        l[L] += 1
        r[R] += 1
    ans = 0
    now = 0
    for i in range(1, N + 1):
        now += l[i]
        if now == M:
            ans += 1
        now -= r[i]
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    l = [0] * (n + 1)
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l[l_i - 1] += 1
        l[r_i] -= 1
    for i in range(1, n + 1):
        l[i] += l[i - 1]
    print(l.count(m))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    arr = [0 for i in range(N+1)]
    for i in range(M):
        l, r = map(int, input().split())
        arr[l-1] += 1
        arr[r] -= 1
    for i in range(1, N+1):
        arr[i] += arr[i-1]
    print(arr.count(M))

=======
Suggestion 9

def main():
    # input
    N, M = map(int, input().split())
    LRs = [[int(i) for i in input().split()] for _ in range(M)]

    # compute
    # 1枚だけで全てのゲートを通過できるIDカードの枚数を出力せよ。
    # 1枚だけで全てのゲートを通過できるIDカードは何枚あるでしょうか。
    # 1枚だけで全てのゲートを通過できるIDカードの枚数を出力せよ。
    # 1枚だけで全てのゲートを通過できるIDカードは何枚あるでしょうか。
    # 1枚だけで全てのゲートを通過できるIDカードの枚数を出力せよ。
    # 1枚だけで全てのゲートを通過できるIDカードは何枚あるでしょうか。
    # 1枚だけで全てのゲートを通過できるIDカードの枚数を出力せよ。
    # 1枚だけで全てのゲートを通過できるIDカードは何枚あるでしょうか。
    # 1枚だけで全てのゲートを通過できるIDカードの枚数を出力せよ。
    # 1枚だけで全てのゲートを通過できるIDカードは何枚あるでしょうか。
    # 1枚だけで全てのゲートを通過できるIDカードの枚数を出力せよ。
    # 1枚だけで全てのゲートを通過できるIDカードは何枚あるでしょうか。
    # 1枚だけで全てのゲートを通過
