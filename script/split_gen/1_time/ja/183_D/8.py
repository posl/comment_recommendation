def main():
    N, W = map(int, input().split())
    # 2次元配列を作成
    # 0:時刻, 1:人数, 2:リットル数
    water = [[0 for i in range(3)] for j in range(N)]
    for i in range(N):
        S, T, P = map(int, input().split())
        water[i][0] = S
        water[i][1] = 1
        water[i][2] = P
        water.append([T, -1, -P])
    water.sort()
    # print(water)
    # print(water[0][0])
    # print(water[0][1])
    # print(water[0][2])
    # print(water[1][0])
    # print(water[1][1])
    # print(water[1][2])
    # print(water[2][0])
    # print(water[2][1])
    # print(water[2][2])
    # print(water[3][0])
    # print(water[3][1])
    # print(water[3][2])
    # print(water[4][0])
    # print(water[4][1])
    # print(water[4][2])
    # print(water[5][0])
    # print(water[5][1])
    # print(water[5][2])
    # print(water[6][0])
    # print(water[6][1])
    # print(water[6][2])
    # print(water[7][0])
    # print(water[7][1])
    # print(water[7][2])
    # print(water[8][0])
    # print(water[8][1])
    # print(water[8][2])
    # print(water[9][0])
    # print(water[9][1])
    # print(water[9][2])
    # print(water[10][0])
    # print(water[10][1])
    # print(water[10][2])
    # print(water[11][0])
    # print(water[11][1])
    # print(water[11][2])
    #
