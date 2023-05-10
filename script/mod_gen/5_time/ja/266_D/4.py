def main():
    n = int(input())
    txa = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    t = 0
    x = 0
    for i in range(n):
        ans = max(ans, txa[i][2])
        if txa[i][2] > txa[i][0] - t + abs(txa[i][1] - x):
            ans = max(ans, (txa[i][2] + txa[i][0] - t + abs(txa[i][1] - x)) // 2)
        t = txa[i][0]
        x = txa[i][1]
    print(ans)

if __name__ == '__main__':
    main()