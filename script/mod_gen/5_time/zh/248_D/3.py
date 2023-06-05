def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    res = []
    for i in range(Q):
        L, R, X = map(int, input().split())
        res.append(A[L-1:R].count(X))
    for i in range(Q):
        print(res[i])

if __name__ == '__main__':
    solve()