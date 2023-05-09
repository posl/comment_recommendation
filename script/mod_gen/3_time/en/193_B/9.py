def main():
    N = int(input())
    shops = [list(map(int, input().split())) for i in range(N)]
    ans = -1
    for i in range(N):
        if shops[i][0] < shops[i][2]:
            if ans == -1:
                ans = shops[i][1]
            else:
                ans = min(ans, shops[i][1])
    print(ans)

if __name__ == '__main__':
    main()