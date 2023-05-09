def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    friends = [[] for _ in range(N+1)]
    blocks = [[] for _ in range(N+1)]
    for a, b in AB:
        friends[a].append(b)
        friends[b].append(a)
    for c, d in CD:
        blocks[c].append(d)
        blocks[d].append(c)
    ans = [0] * (N+1)
    for i in range(1, N+1):
        ans[i] = len(set(friends[i]) & set(friends[i]) - set(blocks[i]) - {i}) - len(set(friends[i]) & set(blocks[i]))
    print(*ans[1:])
