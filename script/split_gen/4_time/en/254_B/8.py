def solution(n):
    arr = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    for i in range(n):
        print(' '.join(map(str, arr[i])))
