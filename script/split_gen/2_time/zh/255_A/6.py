def problems255_a():
    r,c = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(2)]
    print(a[r-1][c-1])
