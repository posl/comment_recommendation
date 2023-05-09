def main():
    #input
    N, K = map(int, input().split())
    P = [[0]*4 for _ in range(N)]
    for i in range(N):
        P[i][0], P[i][1], P[i][2] = map(int, input().split())
    #compute
    for i in range(N):
        P[i][3] = 300 - P[i][2]
    P.sort(key=lambda x: x[0]+x[1]+x[2]+x[3], reverse=True)
    #output
    for i in range(N):
        if P[i][0]+P[i][1]+P[i][2]+P[i][3] >= P[K-1][0]+P[K-1][1]+P[K-1][2]+P[K-1][3]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()