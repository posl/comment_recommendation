def main():
    N, M, K = map(int, input().split())
    friends = [set() for _ in range(N)]
    block = [set() for _ in range(N)]
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
        block[C].add(D)
        block[D].add(C)
    for i in range(N):
        friends[i].add(i)
        block[i].add(i)
    for i in range(N):
        for f in friends[i]:
            block[i] |= block[f]
    for i in range(N):
        print(len(friends[i] & block[i]) - 1, end=' ')
    print()
