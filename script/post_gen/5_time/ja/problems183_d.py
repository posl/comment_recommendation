Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    STP = [list(map(int, input().split())) for _ in range(N)]
    STP.sort()
    T = [0] * (2 * 10**5 + 1)
    for s, t, p in STP:
        T[s] += p
        T[t] -= p
    for i in range(2 * 10**5):
        T[i + 1] += T[i]
        if T[i] > W:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 3

def main():
    n, w = map(int, input().split())
    s = [0] * n
    t = [0] * n
    p = [0] * n

    for i in range(n):
        s[i], t[i], p[i] = map(int, input().split())

    #print(s)
    #print(t)
    #print(p)

    # 各時刻でのお湯の使用量
    use = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        use[s[i]] += p[i]
        use[t[i]] -= p[i]

    #print(use)

    # 各時刻でのお湯の使用量の累積和
    use_cum = [0] * (2 * 10 ** 5 + 1)
    for i in range(2 * 10 ** 5):
        use_cum[i + 1] = use_cum[i] + use[i]

    #print(use_cum)

    # お湯の使用量が W を超えているかどうか
    for i in range(2 * 10 ** 5):
        if use_cum[i] > w:
            print('No')
            return

    print('Yes')

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    S = [0] * N
    T = [0] * N
    P = [0] * N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())
    #print(N, W)
    #print(S)
    #print(T)
    #print(P)

    # 0 <= S[i] < T[i] <= 2 * 10^5
    # 1 <= W, P[i] <= 10^9
    # 1 <= N <= 2 * 10^5
    # 入力はすべて整数
    # 1 <= N <= 2 * 10^5 なので、配列を用いた場合、
    # 2 * 10^5 * 2 * 10^5 = 4 * 10^10 となり、メモリが不足する。
    # そこで、座標圧縮を用いる。
    # 0 <= S[i] < T[i] <= 2 * 10^5 なので、
    # 0 <= S[i] < T[i] <= 2 * 10^5 の範囲にある値のみを
    # 配列に格納するようにする。
    # また、時刻 0 から 2 * 10^5 までの間にお湯を使う人がいるかどうかを
    # 記録する配列を用意する。

    # まず、時刻 0 から 2 * 10^5 までの間にお湯を使う人がいるかどうかを
    # 記録する配列を用意する。
    # 0 <= S[i] < T[i] <= 2 * 10^5 なので、
    # 2 * 10^5 + 1 個の要素を持つ配列を用意する。
    # この配列を A とする。A

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    S = []
    T = []
    P = []
    for i in range(N):
        s, t, p = map(int, input().split())
        S.append(s)
        T.append(t)
        P.append(p)

    #print(N, W)
    #print(S)
    #print(T)
    #print(P)

    #配列の最大値を取得する
    max_t = max(T)
    #print(max_t)

    #最大値分の配列を作成する
    use = [0] * (max_t + 1)
    #print(use)

    #各人の利用量を配列に格納する
    for i in range(N):
        use[S[i]] += P[i]
        use[T[i]] -= P[i]
    #print(use)

    #累積和を取得する
    for i in range(max_t):
        use[i + 1] += use[i]
    #print(use)

    #最大値がWを超えていたらNo
    for i in range(max_t):
        if use[i] > W:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 6

def solve():
    N, W = map(int, input().split())
    imos = [0] * (2 * 10 ** 5 + 1)
    for _ in range(N):
        s, t, p = map(int, input().split())
        imos[s] += p
        imos[t] -= p
    for i in range(2 * 10 ** 5):
        imos[i + 1] += imos[i]
        if imos[i + 1] > W:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def main():
    n, w = map(int, input().split())
    s, t, p = [], [], []
    for i in range(n):
        si, ti, pi = map(int, input().split())
        s.append(si)
        t.append(ti)
        p.append(pi)

    # 0 <= s < t <= 2*10^5
    # 1 <= w, p <= 10^9
    # 1 <= n <= 2*10^5
    # 1 <= s <= 2*10^5
    # 1 <= t <= 2*10^5
    # 1 <= p <= 10^9

    # 0 <= s < t <= 2*10^5
    # 1 <= w, p <= 10^9
    # 1 <= n <= 2*10^5
    # 1 <= s <= 2*10^5
    # 1 <= t <= 2*10^5
    # 1 <= p <= 10^9

    # 0 <= s < t <= 2*10^5
    # 1 <= w, p <= 10^9
    # 1 <= n <= 2*10^5
    # 1 <= s <= 2*10^5
    # 1 <= t <= 2*10^5
    # 1 <= p <= 10^9

    # 0 <= s < t <= 2*10^5
    # 1 <= w, p <= 10^9
    # 1 <= n <= 2*10^5
    # 1 <= s <= 2*10^5
    # 1 <= t <= 2*10^5
    # 1 <= p <= 10^9

    # 0 <= s < t <= 2*10^5
    # 1 <= w, p <= 10^9
    # 1 <= n <= 2*10^5
    # 1 <= s <= 2*10^5
    # 1 <= t <= 2*10^5
    # 1 <= p <= 10^9

    # 0 <= s < t <= 2*10^5
    # 1

=======
Suggestion 8

def resolve():
    N,W = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    A.sort()
    #print(A)

    #print("A[0][0] = ", A[0][0])
    #print("A[0][1] = ", A[0][1])
    #print("A[0][2] = ", A[0][2])
    #print("A[1][0] = ", A[1][0])
    #print("A[1][1] = ", A[1][1])
    #print("A[1][2] = ", A[1][2])

    #print("A[0][0] = ", A[0][0])
    #print("A[0][1] = ", A[0][1])
    #print("A[0][2] = ", A[0][2])
    #print("A[1][0] = ", A[1][0])
    #print("A[1][1] = ", A[1][1])
    #print("A[1][2] = ", A[1][2])

    #print("A[0][0] = ", A[0][0])
    #print("A[0][1] = ", A[0][1])
    #print("A[0][2] = ", A[0][2])
    #print("A[1][0] = ", A[1][0])
    #print("A[1][1] = ", A[1][1])
    #print("A[1][2] = ", A[1][2])

    #print("A[0][0] = ", A[0][0])
    #print("A[0][1] = ", A[0][1])
    #print("A[0][2] = ", A[0][2])
    #print("A[1][0] = ", A[1][0])
    #print("A[1][1] = ", A[1][1])
    #print("A[1][2] = ", A[1][2])

    #print("A[0][0] = ", A[0][0])
    #print("A

=======
Suggestion 9

def main():
    N, W = map(int, input().split())
    STP = [list(map(int, input().split())) for _ in range(N)]

    #print(N)
    #print(W)
    #print(STP)

    #s = [0] * 200001
    #t = [0] * 200001
    #p = [0] * 200001

    #for i in range(N):
    #    s[i], t[i], p[i] = map(int, input().split())

    #print(s)
    #print(t)
    #print(p)

    #print("test")

    #print(STP[0][0])
    #print(STP[0][1])
    #print(STP[0][2])

    #print(STP[1][0])
    #print(STP[1][1])
    #print(STP[1][2])

    #print(STP[2][0])
    #print(STP[2][1])
    #print(STP[2][2])

    #print(STP[3][0])
    #print(STP[3][1])
    #print(STP[3][2])

    #print("test")

    #print(STP[0])

    #print("test")

    #print(STP[0][0])
    #print(STP[0][1])
    #print(STP[0][2])

    #print("test")

    #print(STP[0][0])
    #print(STP[0][1])
    #print(STP[0][2])

    #print("test")

    #print(STP[0][0])
    #print(STP[0][1])
    #print(STP[0][2])

    #print("test")

    #print(STP[0][0])
    #print(STP[0][1])
    #print(STP[0][2])

    #print("test")

    #print(STP[0][0])
    #print(STP[0][1])
    #print(STP[0][2])

    #print("test")

    #print(STP[0][0])
    #print(STP[0][1])
    #print(STP[0][2])

    #print("test")

    #print(STP[0][0])
