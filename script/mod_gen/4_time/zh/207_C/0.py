def main():
    N = int(input())
    tlr = []
    for i in range(N):
        t, l, r = map(int, input().split())
        tlr.append([t, l, r])
    # print(tlr)
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if tlr[i][1] <= tlr[j][1] <= tlr[i][2] or tlr[j][1] <= tlr[i][1] <= tlr[j][2]:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()