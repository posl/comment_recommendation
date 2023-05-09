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
    for i in range(1, M + 1):
        A = [i]
        for j in range(1, N):
            A.append(A[j - 1] + 1)
        score = 0
        for k in range(Q):
            if A[b[k] - 1] - A[a[k] - 1] == c[k]:
                score += d[k]
        ans = max(ans, score)
    print(ans)

if __name__ == '__main__':
    main()