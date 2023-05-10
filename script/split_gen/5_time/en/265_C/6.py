def main():
    h,w = map(int,input().split())
    g = [list(input()) for i in range(h)]
    x,y = 0,0
    while True:
        if g[x][y] == 'R':
            if y == w-1:
                print(x+1,y+1)
                break
            else:
                y += 1
        elif g[x][y] == 'L':
            if y == 0:
                print(x+1,y+1)
                break
            else:
                y -= 1
        elif g[x][y] == 'U':
            if x == 0:
                print(x+1,y+1)
                break
            else:
                x -= 1
        elif g[x][y] == 'D':
            if x == h-1:
                print(x+1,y+1)
                break
            else:
                x += 1
        else:
            print(x+1,y+1)
            break
