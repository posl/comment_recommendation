def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = [-1] * N
    for i in range(M):
        ans[B[i]-1] = A[i]
    for i in range(N):
        if ans[i] == -1:
            ans[i] = i + 1
    if len(set(ans)) != N:
        print(-1)
    else:
        print(' '.join(map(str, ans)))

if __name__ == '__main__':
    solve()