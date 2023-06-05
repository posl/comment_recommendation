def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int,input().split())))
    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if tlr[i][2] < tlr[j][1]:
                continue
            if tlr[j][2] < tlr[i][1]:
                continue
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()