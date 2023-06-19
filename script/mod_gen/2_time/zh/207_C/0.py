def main():
    n = int(input())
    tlr = []
    for _ in range(n):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if tlr[i][1] <= tlr[j][1] and tlr[i][2] >= tlr[j][1]:
                ans += 1
            elif tlr[i][1] >= tlr[j][1] and tlr[i][1] <= tlr[j][2]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()