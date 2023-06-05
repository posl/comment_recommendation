def getNumOfLikeFood():
    N, M = map(int, input().split())
    num = 0
    food = [0] * M
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(1, temp[0] + 1):
            food[temp[j] - 1] += 1
    for i in range(M):
        if food[i] == N:
            num += 1
    print(num)
getNumOfLikeFood()
