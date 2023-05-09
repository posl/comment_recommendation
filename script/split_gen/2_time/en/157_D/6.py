def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N+1)]
    blocks = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c].append(d)
        blocks[d].append(c)
    for i in range(1, N+1):
        ans = N - len(friends[i]) - 1
        for b in blocks[i]:
            if b in friends[i]:
                ans -= 1
        print(ans, end=" ")
