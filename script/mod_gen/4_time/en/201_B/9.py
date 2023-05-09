def getSecondHighestMountainName():
    N = int(input())
    mountainNameHeightList = []
    for i in range(N):
        mountainNameHeightList.append(input().split())
    mountainNameHeightList.sort(key=lambda x: x[1], reverse=True)
    return mountainNameHeightList[1][0]

if __name__ == '__main__':
    getSecondHighestMountainName()