def main():
    N,M = map(int,input().split())
    P_Y = [list(map(int,input().split())) for i in range(M)]
    P_Y.sort(key=lambda x:x[1])
    city = {i:[] for i in range(1,N+1)}
    for p,y in P_Y:
        city[p].append(y)
    for p,y in P_Y:
        print("%06d%06d"%(p,city[p].index(y)+1))
