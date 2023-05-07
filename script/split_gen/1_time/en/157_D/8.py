def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocked = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A - 1].append(B - 1)
        friends[B - 1].append(A - 1)
    for _ in range(K):
        C, D = map(int, input().split())
        blocked[C - 1].append(D - 1)
        blocked[D - 1].append(C - 1)
    result = [0] * N
    for i in range(N):
        result[i] = N - len(friends[i]) - 1
        for j in friends[i]:
            if i in friends[j]:
                result[i] -= 1
        for j in blocked[i]:
            if j in friends[i]:
                result[i] -= 1
    print(*result)
