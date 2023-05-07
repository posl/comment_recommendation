def solve():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s - 1][t])

if __name__ == '__main__':
    solve()