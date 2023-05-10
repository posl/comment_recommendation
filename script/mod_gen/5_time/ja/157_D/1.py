def solve():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)
    for _ in range(K):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        blocks[c].append(d)
        blocks[d].append(c)
    ans = [0] * N
    for i in range(N):
        ans[i] = len(set(friends[i]) - set(friends[i]) & set(blocks[i]) - {i}) - 1
    print(*ans)

if __name__ == '__main__':
    solve()