def main():
    n,m = map(int,input().split())
    s = [[-1 for i in range(n)] for j in range(n)]
    s[0][0] = 0
    q = [[0,0]]
    while len(q) > 0:
        x,y = q.pop(0)
        for i in range(n):
            for j in range(n):
                if s[i][j] == -1:
                    if abs(x-i)**2 + abs(y-j)**2 == m:
                        s[i][j] = s[x][y] + 1
                        q.append([i,j])
    for i in range(n):
        for j in range(n):
            print(s[i][j], end = ' ')
        print()
