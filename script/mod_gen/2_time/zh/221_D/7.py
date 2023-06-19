def solve():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [0] * N
    for i in range(N):
        ans[i] = A[i] + B[i] - 1
    ans.sort()
    for i in range(N):
        print(ans[i], end=' ')
    print()

if __name__ == '__main__':
    solve()