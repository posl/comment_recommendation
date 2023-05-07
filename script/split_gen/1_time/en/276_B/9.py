def main():
    N, M = map(int, input().split())
    #print(N,M)
    #print("
")
    road = []
    for i in range(M):
        road.append(list(map(int, input().split())))
    #print(road)
    #print("
")
    d = {}
    for i in range(1,N+1):
        #print(i)
        d[i] = []
        for j in range(M):
            #print(j)
            if i in road[j]:
                if i == road[j][0]:
                    d[i].append(road[j][1])
                else:
                    d[i].append(road[j][0])
        d[i].sort()
        print(len(d[i]),end = " ")
        for k in d[i]:
            print(k,end = " ")
        print("
")
