def main():
    N, M, K = map(int, input().split())
    friends = []
    blocks = []
    for i in range(M):
        friends.append(list(map(int, input().split())))
    for i in range(K):
        blocks.append(list(map(int, input().split())))
    #print(N, M, K)
    #print(friends)
    #print(blocks)
    candidates = [0] * N
    for i in range(N):
        for j in range(M):
            if friends[j][0] == i + 1:
                candidates[i] += 1
            if friends[j][1] == i + 1:
                candidates[i] += 1
    #print(candidates)
    for i in range(N):
        for j in range(K):
            if blocks[j][0] == i + 1:
                candidates[i] -= 1
            if blocks[j][1] == i + 1:
                candidates[i] -= 1
    #print(candidates)
    for i in range(N):
        for j in range(M):
            if friends[j][0] == i + 1:
                candidates[i] -= 1
            if friends[j][1] == i + 1:
                candidates[i] -= 1
    #print(candidates)
    for i in range(N):
        for j in range(K):
            if blocks[j][0] == i + 1:
                candidates[i] += 1
            if blocks[j][1] == i + 1:
                candidates[i] += 1
    #print(candidates)
    for i in range(N):
        print(candidates[i], end=' ')
main()
