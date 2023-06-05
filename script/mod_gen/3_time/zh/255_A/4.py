def problems255_a():
    R,C = map(int,input().split())
    a = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        a[i] = list(map(int,input().split()))
    print(a[R-1][C-1])
problems255_a()
