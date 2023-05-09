def main():
    h,w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    i = 0
    j = 0
    while True:
        if g[i][j] == 'U':
            if i != 0:
                i = i - 1
            else:
                print(i+1, j+1)
                break
        elif g[i][j] == 'D':
            if i != h-1:
                i = i + 1
            else:
                print(i+1, j+1)
                break
        elif g[i][j] == 'L':
            if j != 0:
                j = j - 1
            else:
                print(i+1, j+1)
                break
        elif g[i][j] == 'R':
            if j != w-1:
                j = j + 1
            else:
                print(i+1, j+1)
                break
        else:
            print(-1)
            break
