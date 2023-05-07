def solve():
    N, M = map(int, input().split())
    D = [0] * N
    for i in range(M):
        a, b = map(int, input().split())
        D[a-1] += 1
        D[b-1] += 1
    ans = 0
    for i in range(N):
        ans += D[i]*(D[i]-1)//2
    print(ans)

if __name__ == '__main__':
    solve()