def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    A.append(N+1)
    B.append(N+1)
    ans = 0
    j = 0
    for i in range(1, N+2):
        while A[j] < i:
            j += 1
        ans = max(ans, j - i + 1)
    print(ans)

if __name__ == '__main__':
    solve()