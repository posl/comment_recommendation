def main():
    N = int(input())
    jump = []
    for i in range(N):
        jump.append(list(map(int, input().split())))
    jump.sort(key=lambda x: x[2])
    #print(jump)
    d = [[float("inf")]*N for i in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            d[i][j] = abs(jump[i][0]-jump[j][0])+abs(jump[i][1]-jump[j][1])
            d[j][i] = d[i][j]
    #print(d)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j] > d[i][k]+d[k][j]:
                    d[i][j] = d[i][k]+d[k][j]
    #print(d)
    ans = 0
    for i in range(N):
        for j in range(N):
            if d[i][j] <= jump[i][2]:
                ans = max(ans, jump[i][2])
    print(ans)

if __name__ == '__main__':
    main()