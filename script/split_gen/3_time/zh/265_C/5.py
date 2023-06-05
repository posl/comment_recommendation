def main():
    h,w = map(int,input().split())
    g = [list(input()) for _ in range(h)]
    i,j = 0,0
    while True:
        if g[i][j] == "U":
            if i == 0:
                print(i+1,j+1)
                return
            else:
                i -= 1
        elif g[i][j] == "D":
            if i == h-1:
                print(i+1,j+1)
                return
            else:
                i += 1
        elif g[i][j] == "L":
            if j == 0:
                print(i+1,j+1)
                return
            else:
                j -= 1
        elif g[i][j] == "R":
            if j == w-1:
                print(i+1,j+1)
                return
            else:
                j += 1
        else:
            print(i+1,j+1)
            return
    print(-1)
