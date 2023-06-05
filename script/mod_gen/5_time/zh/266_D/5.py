def main():
    n = int(input())
    txa = []
    for i in range(n):
        txa.append([int(j) for j in input().split()])
    txa.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            if txa[i][1] >= txa[i][0]:
                ans += txa[i][2]
                now = txa[i][0]
                size = txa[i][2]
            else:
                now = txa[i][0]
                size = txa[i][2]
        else:
            now += txa[i][0] - txa[i - 1][0]
            if txa[i][1] >= now:
                ans += txa[i][2]
                now = txa[i][0]
                size = txa[i][2]
            else:
                if txa[i][1] + size >= now:
                    ans += txa[i][2] - (now - txa[i][1])
                    now = txa[i][0]
                    size = txa[i][2]
    print(ans)

if __name__ == '__main__':
    main()