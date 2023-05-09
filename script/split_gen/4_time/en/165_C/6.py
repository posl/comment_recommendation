def main():
    N, M, Q = map(int, input().split())
    A = [0] * (N+1)
    A[0] = 1
    A[N] = M
    q = []
    for i in range(Q):
        q.append(list(map(int, input().split())))
    print(calc(N, M, q, A))
