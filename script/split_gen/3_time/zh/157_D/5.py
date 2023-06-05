def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    blocks = [[] for _ in range(N)]
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
    candidate = [0] * N
    for i in range(N):
        for j in friends[i]:
            candidate[i] += 1
        for j in blocks[i]:
            candidate[i] -= 1
        candidate[i] -= 1
    print(" ".join(map(str, candidate)))
