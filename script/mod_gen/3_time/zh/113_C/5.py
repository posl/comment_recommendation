def main():
    N,M = map(int,input().split())
    P_Y = [list(map(int,input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x:x[1])
    #print(P_Y)
    city = [0]*N
    for i in range(M):
        city[P_Y[i][0]-1] += 1
    #print(city)
    for i in range(M):
        print(str(P_Y[i][0]).zfill(6)+str(city[P_Y[i][0]-1]).zfill(6))

if __name__ == '__main__':
    main()