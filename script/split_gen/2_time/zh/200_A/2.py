def main():
    n,m = map(int,input().split())
    edge = [list(map(int,input().split())) for i in range(m)]
    #print(edge)
    #print(n,m)
    #print(edge)
    color = [0 for i in range(n)]
    #print(color)
    cnt = 0
    for i in range(3**n):
        for j in range(n):
            color[j] = (i//(3**j))%3
        #print(color)
        ok = True
        for j in range(m):
            if color[edge[j][0]-1] == color[edge[j][1]-1]:
                ok = False
        if ok:
            cnt += 1
    print(cnt)
