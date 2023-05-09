def main():
    #入力
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(XY)
    #組み合わせの計算
    import itertools
    comb = list(itertools.combinations(XY, 3))
    # print(comb)
    #三角形の判定
    count = 0
    for i in range(len(comb)):
        # print(comb[i])
        x1 = comb[i][0][0]
        y1 = comb[i][0][1]
        x2 = comb[i][1][0]
        y2 = comb[i][1][1]
        x3 = comb[i][2][0]
        y3 = comb[i][2][1]
        # print(x1, y1, x2, y2, x3, y3)
        if (x1 - x2) * (y2 - y3) - (y1 - y2) * (x2 - x3) != 0:
            count += 1
        # else:
        #     print('三角形ではない')
    #出力
    print(count)
