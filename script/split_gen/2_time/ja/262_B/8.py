def main():
    n,m = map(int, input().split())
    edge = []
    for i in range(m):
        u,v = map(int, input().split())
        edge.append((u,v))
    #print(edge)
    cnt = 0
    for i in range(m):
        for j in range(i+1, m):
            #print(i,j)
            u1,v1 = edge[i]
            u2,v2 = edge[j]
            if u1 == u2 or u1 == v2 or v1 == u2 or v1 == v2:
                #print(u1,v1,u2,v2)
                cnt += 1
    print(cnt)
