def main():
    N, M, Q = map(int, input().split())
    a, b, c, d = [], [], [], []
    for i in range(Q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    ans = 0
    for i in range(M):
        A = [i+1]
        for j in range(1, N):
            A.append(A[j-1]+1)
        for j in range(Q):
            if A[b[j]-1]-A[a[j]-1] == c[j]:
                ans += d[j]
    print(ans)

if __name__ == '__main__':
    main()