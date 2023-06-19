def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    #print(tlr)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][1] <= tlr[j][1] <= tlr[i][2] or tlr[i][1] <= tlr[j][2] <= tlr[i][2] or tlr[j][1] <= tlr[i][1] <= tlr[j][2] or tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()