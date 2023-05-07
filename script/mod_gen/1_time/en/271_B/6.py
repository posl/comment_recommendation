def solve():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        L, *a = list(map(int, input().split()))
        A.append(a)
    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])
solve()

if __name__ == '__main__':
    solve()