def getSecondMaxMountainName():
    mountains = []
    N = int(input())
    for i in range(N):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])
getSecondMaxMountainName()
