def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    # x座標を基準にソート
    points.sort(key=lambda x: x[0])
    # x座標が同じものをグループ化
    x_group = []
    tmp = []
    for i in range(N):
        if i == 0:
            tmp.append(points[0])
        else:
            if points[i][0] == points[i - 1][0]:
                tmp.append(points[i])
            else:
                x_group.append(tmp)
                tmp = []
                tmp.append(points[i])
    x_group.append(tmp)
    # y座標を基準にソート
    for i in range(len(x_group)):
        x_group[i].sort(key=lambda x: x[1])
    # y座標が同じものをグループ化
    y_group = []
    for i in range(len(x_group)):
        tmp = []
        for j in range(len(x_group[i])):
            if j == 0:
                tmp.append(x_group[i][0])
            else:
                if x_group[i][j][1] == x_group[i][j - 1][1]:
                    tmp.append(x_group[i][j])
                else:
                    y_group.append(tmp)
                    tmp = []
                    tmp.append(x_group[i][j])
        y_group.append(tmp)
    # それぞれのグループの中から2点を選ぶ組み合わせを求める
    ans = 0
    for i in range(len(y_group)):
        ans += (len(y_group[i]) * (len(y_group[i]) - 1)) // 2
    print(ans)

if __name__ == '__main__':
    main()