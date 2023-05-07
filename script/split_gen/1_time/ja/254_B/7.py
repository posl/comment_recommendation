def main():
    N = int(input())
    #N = 3
    #N = 10
    a = [[1] * i for i in range(1, N + 1)]
    for i in range(1, N):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in range(N):
        print(*a[i])
