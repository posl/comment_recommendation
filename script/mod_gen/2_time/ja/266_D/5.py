def main():
    N = int(input())
    txa = [list(map(int, input().split())) for _ in range(N)]
    #print(txa)
    ans = 0
    for i in range(N):
        #print(txa[i][0])
        #print(txa[i][1])
        #print(txa[i][2])
        for j in range(i+1, N):
            #print(txa[j][0])
            #print(txa[j][1])
            #print(txa[j][2])
            if txa[i][0] + abs(txa[i][1] - txa[j][1]) <= txa[j][0]:
                ans += txa[i][2]
                #print(ans)
            if txa[j][0] + abs(txa[i][1] - txa[j][1]) <= txa[i][0]:
                ans += txa[j][2]
                #print(ans)
    print(ans)

if __name__ == '__main__':
    main()