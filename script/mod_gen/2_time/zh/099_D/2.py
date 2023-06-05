def readinput():
    n,c = map(int,input().split())
    d = []
    for i in range(c):
        d.append(list(map(int,input().split())))
    grid = []
    for i in range(n):
        grid.append(list(map(int,input().split())))
    return n,c,d,grid

if __name__ == '__main__':
    readinput()