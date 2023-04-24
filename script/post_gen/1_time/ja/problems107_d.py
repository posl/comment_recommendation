Synthesizing 8/10 solutions

=======
Suggestion 1

def median3(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return b

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    C = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = C[i] + B[i + 1]
    ans = 0
    for i in range(N):
        ans += (B[i + 1] - B[i]) * (C[N] - C[i + 1])
    print(ans)
    return

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(N):
        m.append(a[i])
        for j in range(i + 1, N):
            m.append(min(a[i:j + 1]))
    m.sort()
    print(m[int(len(m) / 2)])

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N):
        b[i] = a[i]
    b.sort()
    c = [0] * N
    for i in range(N):
        c[i] = b[i]
    for i in range(N):
        c[i] = c[i] + c[i - 1]
    d = [0] * N
    for i in range(N):
        d[i] = c[i]
    for i in range(N):
        d[i] = d[i] - c[i - 1]
    e = [0] * N
    for i in range(N):
        e[i] = d[i]
    for i in range(N):
        e[i] = e[i] + e[i - 1]
    f = [0] * N
    for i in range(N):
        f[i] = e[i]
    for i in range(N):
        f[i] = f[i] - e[i - 1]
    g = [0] * N
    for i in range(N):
        g[i] = f[i]
    for i in range(N):
        g[i] = g[i] + g[i - 1]
    h = [0] * N
    for i in range(N):
        h[i] = g[i]
    for i in range(N):
        h[i] = h[i] - g[i - 1]
    i = [0] * N
    for i in range(N):
        i[i] = h[i]
    for i in range(N):
        i[i] = i[i] + i[i - 1]
    j = [0] * N
    for i in range(N):
        j[i] = i[i]
    for i in range(N):
        j[i] = j[i] - i[i - 1]
    k = [0] * N
    for i in range(N):
        k[i] = j[i]
    for i in range(N):
        k[i] = k[i] + k[i - 1]
    l = [0] * N
    for i in range(N):
        l[i] = k[i]
    for i in range(N):
        l[i] = l[i]

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        print(a[0])
        return
    b = [0] * N
    for i in range(N):
        b[i] = (a[i], i)
    b.sort()
    c = [0] * N
    for i in range(N):
        c[b[i][1]] = i
    seg = SegmentTree(N, min)
    seg.update(0, N, 0)
    for i in range(N):
        seg.update(c[i], c[i] + 1, i)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += seg.query(i, j + 1)
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    c = [0] * n
    for i in range(n):
        c[i] = b[i // 2]
        if i % 2 == 1:
            c[i] = -c[i]
    d = [0] * n
    for i in range(n):
        d[i] = c[i] + d[i - 1]
    e = [0] * n
    for i in range(n):
        e[i] = a[i] + e[i - 1]
    ans = 0
    for i in range(n):
        ans += (i + 1) * a[i] - e[i]
        ans += (n - i - 1) * a[i] - (e[n - 1] - e[i])
        ans += d[i] * a[i]
        ans -= (d[i] - d[0]) * a[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 中央値の候補
    cand = []
    for i in range(N):
        cand.append(A[i])
        if i >= 1:
            cand.append((A[i] + A[i-1]) // 2)
    cand.append(A[-1])

    # 中央値の候補の中で、各要素が何個含まれているかを数える
    cnt = [0] * (N+1)
    for a in A:
        cnt[a] += 1

    # 中央値の候補の中で、各要素が何個含まれているかの累積和を取る
    cnt_cumsum = [0] * (N+1)
    for i in range(N):
        cnt_cumsum[i+1] = cnt_cumsum[i] + cnt[i]

    # 中央値の候補の中で、各要素が何個含まれているかの累積和の逆順の累積和を取る
    cnt_cumsum_rev = [0] * (N+1)
    for i in range(N):
        cnt_cumsum_rev[i+1] = cnt_cumsum_rev[i] + cnt[N-i-1]

    # 中央値の候補の中で、各要素が何個含まれているかの累積和の逆順の累積和の逆順を取る
    cnt_cumsum_rev_rev = [0] * (N+1)
    for i in range(N):
        cnt_cumsum_rev_rev[i+1] = cnt_cumsum_rev_rev[i] + cnt_cumsum_rev[N-i-1]

    # 中央値の候補の中で、各要素が何個含まれているかの累積和の逆順の累積和の逆順を取る
    cnt_cumsum_rev_rev_rev = [0] * (N+1

=======
Suggestion 8

def median(lst):
    lst.sort()
    return lst[len(lst) // 2]
