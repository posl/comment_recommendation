def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]) or (tlr[i][1] <= tlr[j][2] and tlr[j][2] <= tlr[i][2]) or (tlr[j][1] <= tlr[i][1] and tlr[i][1] <= tlr[j][2]) or (tlr[j][1] <= tlr[i][2] and tlr[i][2] <= tlr[j][2]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()