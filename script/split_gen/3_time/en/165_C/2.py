def main():
    N, M, Q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(Q):
        x, y, z, w = map(int, input().split())
        a.append(x)
        b.append(y)
        c.append(z)
        d.append(w)
    A = [1] * N
    ans = 0
    while True:
        score = 0
        for i in range(Q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                score += d[i]
        ans = max(ans, score)
        i = N - 1
        while i >= 0 and A[i] == M:
            i -= 1
        if i < 0:
            break
        A[i] += 1
        for j in range(i + 1, N):
            A[j] = A[i]
    print(ans)
