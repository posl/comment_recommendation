def main():
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort()
    #print(AB)
    #print("AB[0][1]=", AB[0][1])
    D = [0] * N
    #print("D=", D)
    for i in range(1, N):
        #print("i=", i)
        if AB[i][0] <= AB[i-1][0] + AB[i-1][1] - 1:
            #print("AB[i][0]=", AB[i][0], "AB[i-1][0]=", AB[i-1][0], "AB[i-1][1]=", AB[i-1][1])
            #print("AB[i][0]=", AB[i][0], "AB[i-1][0] + AB[i-1][1] - 1=", AB[i-1][0] + AB[i-1][1] - 1)
            AB[i][1] = AB[i][1] - (AB[i-1][0] + AB[i-1][1] - AB[i][0])
            AB[i][0] = AB[i-1][0] + AB[i-1][1]
            #print("AB[i][0]=", AB[i][0], "AB[i][1]=", AB[i][1])
    #print(AB)
    for i in range(N):
        D[i] = AB[i][1]
    #print("D=", D)
    for i in range(1, N):
        D[i] += D[i-1]
    #print("D=", D)
    for i in range(N):
        D[i] = D[i] + 10**100 - AB[i][0] - AB[i][1] + 1
    #print("D=", D)
    print(*D)

if __name__ == '__main__':
    main()