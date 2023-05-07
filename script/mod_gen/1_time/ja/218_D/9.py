def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    # x座標でソート
    points.sort()
    # y座標でソート
    points_y = sorted(points, key=lambda x: x[1])
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            # x座標を固定
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:
                continue
            # y座標がx1からx2の間にある点の個数
            cnt = 0
            for k in range(N):
                x3, y3 = points_y[k]
                if x1 <= x3 <= x2 and y1 <= y3 <= y2:
                    cnt += 1
            ans += cnt * (cnt - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()