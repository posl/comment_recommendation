def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A, B = A-1, B-1
        friends[A].append(B)
        friends[B].append(A)
    for _ in range(K):
        C, D = map(int, input().split())
        C, D = C-1, D-1
        blocks[C].append(D)
        blocks[D].append(C)
    ans = [0]*N
    for i in range(N):
        ans[i] = len(set(friends[i]) - set(friends[i]) & set(blocks[i]))
    print(*ans)
