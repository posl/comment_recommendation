def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    # マスの座標をグループ化
    XY_group = {}
    for x, y in XY:
        if x not in XY_group:
            XY_group[x] = [y]
        else:
            XY_group[x].append(y)
    # グループの中の座標をソート
    for x in XY_group:
        XY_group[x].sort()
    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])-1):
            XY.append([x, XY_group[x][i]+1])
    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])-1):
            XY.append([x, XY_group[x][i]-1])
    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])):
            XY.append([x+1, XY_group[x][i]])
            XY.append([x-1, XY_group[x][i]])
            XY.append([x+1, XY_group[x][i]+1])
            XY.append([x-1, XY_group[x][i]-1])
    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])-1):
            XY.append([x+1, XY_group[x][i]+1])
            XY.append([x-1, XY_group[x][i]-1])
    # グループの座標を繋げる
    for x in XY_group:
        for i in range(len(XY_group[x])-1):
            XY.append([x+1, XY_group[x][i]-1])
            XY.append([x-1, XY_group[x][i]+1])
    # グループの座標を繋げる
    for x in XY

if __name__ == '__main__':
    main()