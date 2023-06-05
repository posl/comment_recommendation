def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = float('inf')
    for i in range(N):
        t = X * A[i] + B[i]
        ans = min(ans, t)
    print(ans)

if __name__ == '__main__':
    solve()