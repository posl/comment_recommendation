def main():
    N, M, Q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(Q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    ans = 0
    for A in combinations_with_replacement(range(1, M + 1), N):
        score = 0
        for i in range(Q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                score += d[i]
        ans = max(ans, score)
    print(ans)
