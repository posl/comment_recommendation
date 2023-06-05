def main():
    # 读入数据
    N, M = map(int, input().split())
    PY = []
    for i in range(M):
        PY.append(list(map(int, input().split())))
    # 对数据排序
    PY = sorted(PY, key=lambda x: x[1])
    # 生成ID
    id = []
    for i in range(M):
        # 生成P
        P = str(PY[i][0])
        while len(P) < 6:
            P = '0' + P
        # 生成Y
        Y = str(PY[i][1])
        while len(Y) < 6:
            Y = '0' + Y
        # 生成ID
        id.append(P + Y)
    # 输出ID
    for i in range(M):
        print(id[i])

if __name__ == '__main__':
    main()