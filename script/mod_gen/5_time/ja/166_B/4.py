def solve():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        A.append(list(map(int, input().split())))
    B = [0] * N
    for i in range(K):
        for j in range(A[i][0]):
            B[A[i][j+1]-1] += 1
    ans = 0
    for i in range(N):
        if B[i] == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()