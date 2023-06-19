def main():
    h,w,r,c = map(int,input().split())
    n = int(input())
    wall = [[0 for i in range(w+1)] for j in range(h+1)]
    for i in range(n):
        x,y = map(int,input().split())
        wall[x][y] = 1
    q = int(input())
    move = []
    for i in range(q):
        d,l = input().split()
        move.append((d,int(l)))
    #print(wall)
    #print(move)
    #print(q)
    #print(h,w,r,c)
    #print(n)
    #print(wall)
    #print(move)
    #print(q)
    direction = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
    result = []
    for i in range(q):
        x,y = direction[move[i][0]]
        for j in range(move[i][1]):
            r += x
            c += y
            if wall[r][c] == 1:
                r -= x
                c -= y
        result.append((r,c))
    for i in result:
        print(i[0],i[1])

if __name__ == '__main__':
    main()