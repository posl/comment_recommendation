def main():
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
    for i in range(N):
        ans = len(friends[i])
        for j in blocks[i]:
            if j in friends[i]:
                ans -= 1
        for j in friends[i]:
            for k in friends[j]:
                if k != i and k not in friends[i] and k not in blocks[i]:
                    ans += 1
        print(ans, end=" ")
    print()
