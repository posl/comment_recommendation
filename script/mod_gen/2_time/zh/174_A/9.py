def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    cumsum = [0]
    for i in range(2 * N):
        cumsum.append(cumsum[-1] + A[i])
    ans = 0
    for i in range(N):
        ans = max(ans, cumsum[i + N] - cumsum[i + 1] + min(A[i], A[i + N]))
    print(ans)

if __name__ == '__main__':
    solve()