def getMaxSize(n, txa):
    max_size = 0
    x = 0
    for i in range(n):
        if txa[i][0] < txa[i][1] - x:
            x = txa[i][1]
            max_size += txa[i][2]
    return max_size
n = int(input())
txa = []
for i in range(n):
    txa.append(list(map(int, input().split())))
print(getMaxSize(n, txa))
