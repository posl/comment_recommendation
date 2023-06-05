def main():
    n = int(input())
    tlr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()