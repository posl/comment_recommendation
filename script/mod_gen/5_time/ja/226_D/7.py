def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            x = x1 - x2
            y = y1 - y2
            if x < 0:
                x = -x
            if y < 0:
                y = -y
            ans = max(ans, x + y)
    print(ans)

if __name__ == '__main__':
    main()