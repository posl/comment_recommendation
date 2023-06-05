def problems254_b():
    N = int(input())
    arr = [[0 for i in range(N)] for i in range(N)]
    arr[0][0] = 1
    for i in range(1, N):
        arr[i][0] = 1
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=" ")
        print()
problems254_b()
