def main():
    N, M = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(M)]
    #print(N)
    #print(M)
    #print(x)
    #print(x[0][0])
    #print(x[0][1])
    #print(x[1][0])
    #print(x[1][1])
    #print(x[2][0])
    #print(x[2][1])
    for i in range(M-1):
        for j in range(i+1, M):
            #print(i, j)
            #print(x[i][0], x[j][0])
            #print(x[i][1], x[j][1])
            if x[i][0] != x[j][0] and x[i][0] != x[j][1] and x[i][1] != x[j][0] and x[i][1] != x[j][1]:
                print('No')
                exit()
    print('Yes')
