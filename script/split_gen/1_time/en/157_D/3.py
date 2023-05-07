def main():
    N, M, K = map(int, input().split())
    friends = [set() for _ in range(N)]
    blocks = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        friends[A].add(B)
        friends[B].add(A)
    for _ in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        blocks[C].add(D)
        blocks[D].add(C)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1 - len(friends[i]) - len(blocks[i])
        for j in friends[i]:
            if i in blocks[j]:
                ans[i] -= 1
        ans[i] -= 1
    print(*ans)
