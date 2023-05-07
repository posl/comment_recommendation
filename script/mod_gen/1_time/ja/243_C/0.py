def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    # 0:R 1:L
    L = [0] * N
    R = [0] * N
    for i in range(N):
        if S[i] == 'L':
            L[i] = 1
        else:
            R[i] = 1
    # 線分を構成する2点の座標を格納するリスト
    line = []
    for i in range(N):
        if L[i] == 1:
            line.append((X[i], Y[i]))
        if R[i] == 1:
            line.append((X[i], Y[i]))
    # 線分を構成する2点の座標をソート
    line.sort(key=lambda x: x[0])
    # 線分を構成する2点の座標をもとに、線分の傾きと切片を計算
    k = []
    b = []
    for i in range(0, len(line), 2):
        if line[i + 1][0] - line[i][0] == 0:
            k.append(0)
            b.append(0)
        else:
            k.append((line[i + 1][1] - line[i][1]) / (line[i + 1][0] - line[i][0]))
            b.append(line[i][1] - k[i // 2] * line[i][0])
    # 線分の傾きと切片をもとに、線分の交点を計算
    cross_point = []
    for i in range(len(k) - 1):
        if k[i] == k[i + 1]:
            continue
        else:
            cross_point.append((int((b[i + 1] - b[i]) / (k[i] - k[i + 1])), int(k[i] * (b[i + 1] - b[i]) / (k[i] - k[i +

if __name__ == '__main__':
    main()