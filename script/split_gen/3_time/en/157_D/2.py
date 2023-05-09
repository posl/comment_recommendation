def solve():
    N, M, K = map(int, input().split())
    friends = [set() for _ in range(N)]
    blocks = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a - 1].add(b - 1)
        friends[b - 1].add(a - 1)
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c - 1].add(d - 1)
        blocks[d - 1].add(c - 1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friends[i]) - 1
        for j in friends[i]:
            ans[i] -= len(friends[j] & blocks[i])
    for i in range(N):
        print(ans[i], end=" ")
