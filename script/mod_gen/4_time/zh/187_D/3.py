def solve():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N-1, -1, -1):
        A[i] += ans
        if A[i] < B[i]:
            ans += B[i] - A[i]
            A[i] = B[i]
    print(ans)

if __name__ == '__main__':
    solve()