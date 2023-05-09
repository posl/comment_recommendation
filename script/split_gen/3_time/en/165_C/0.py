def main():
    N, M, Q = map(int, input().split())
    a, b, c, d = [], [], [], []
    for i in range(Q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    print(solve(N, M, Q, a, b, c, d))
