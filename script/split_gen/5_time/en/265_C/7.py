def solve():
    h,w = map(int,input().split())
    g = []
    for i in range(h):
        g.append(input())
    i,j = 0,0
    while True:
        if g[i][j] == "R":
            if j == w-1:
                print(i+1,j+1)
                return
            j += 1
        elif g[i][j] == "L":
            if j == 0:
                print(i+1,j+1)
                return
            j -= 1
        elif g[i][j] == "U":
            if i == 0:
                print(i+1,j+1)
                return
            i -= 1
        elif g[i][j] == "D":
            if i == h-1:
                print(i+1,j+1)
                return
            i += 1
        else:
            print(-1)
            return
