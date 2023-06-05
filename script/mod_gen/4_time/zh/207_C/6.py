def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int,input().split())))
    cnt=0
    for i in range(N-1):
        for j in range(i+1,N):
            if tlr[i][2]>=tlr[j][1] and tlr[i][1]<=tlr[j][2]:
                cnt+=1
    print(cnt)

if __name__ == '__main__':
    main()