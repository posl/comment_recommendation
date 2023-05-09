def main():
    h,w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    i,j = 0,0
    while True:
        if g[i][j] == 'U':
            if i == 0:
                break
            else:
                i-=1
        elif g[i][j] == 'D':
            if i == h-1:
                break
            else:
                i+=1
        elif g[i][j] == 'L':
            if j == 0:
                break
            else:
                j-=1
        elif g[i][j] == 'R':
            if j == w-1:
                break
            else:
                j+=1
        else:
            break
    print(i+1,j+1)

if __name__ == '__main__':
    main()