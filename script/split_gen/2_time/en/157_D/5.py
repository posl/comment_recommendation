def solve():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A-1].append(B-1)
        friends[B-1].append(A-1)
    for _ in range(K):
        C, D = map(int, input().split())
        blocks[C-1].append(D-1)
        blocks[D-1].append(C-1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friends[i]) - 1
        for j in friends[i]:
            if i in friends[j]:
                ans[i] -= 1
        for j in blocks[i]:
            if j in friends[i]:
                ans[i] -= 1
    print(*ans)
