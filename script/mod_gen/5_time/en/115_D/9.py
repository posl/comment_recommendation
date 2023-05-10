def countPatty(n, x):
    if n == 0:
        return 1
    elif x == 1:
        return 0
    elif x <= 1 + totalLayers[n-1]:
        return countPatty(n-1, x-1)
    else:
        return 1 + patty[n-1] + countPatty(n-1, x-2-totalLayers[n-1])
patty = [0] * 51
totalLayers = [0] * 51
patty[0] = 1
totalLayers[0] = 1
for i in range(1, 51):
    patty[i] = 2 * patty[i-1] + 1
    totalLayers[i] = 2 * totalLayers[i-1] + 3
n, x = map(int, input().split())
print(countPatty(n, x))

if __name__ == '__main__':
    countPatty()