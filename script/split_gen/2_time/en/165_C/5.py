def main():
    N, M, Q = map(int, input().split())
    A = [0] * (N + 1)
    d = [0] * (N + 1)
    for i in range(Q):
        a, b, c, dd = map(int, input().split())
        if A[a] == 0:
            A[a] = c
            d[a] = dd
        else:
            if A[a] > c:
                A[a] = c
                d[a] = dd
    print(A)
    print(d)
