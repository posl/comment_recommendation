def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    C = [list(map(int, input().split())) for _ in range(N)]
    # 3色でグループ分け
    C1 = []
    C2 = []
    C3 = []
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                C1.append(C[i][j])
            elif (i + j) % 3 == 1:
                C2.append(C[i][j])
            else:
                C3.append(C[i][j])
    # 3色でグループ分けしたものを、色ごとにグループ分け
    C1_1 = []
    C1_2 = []
    C1_3 = []
    C2_1 = []
    C2_2 = []
    C2_3 = []
    C3_1 = []
    C3_2 = []
    C3_3 = []
    for i in range(len(C1)):
        if C1[i] == 1:
            C1_1.append(i)
        elif C1[i] == 2:
            C1_2.append(i)
        else:
            C1_3.append(i)
    for i in range(len(C2)):
        if C2[i] == 1:
            C2_1.append(i)
        elif C2[i] == 2:
            C2_2.append(i)
        else:
            C2_3.append(i)
    for i in range(len(C3)):
        if C3[i] == 1:
            C3_1.append(i)
        elif C3[i] == 2:
            C3_2.append(i)
        else:
            C3_3.append(i)
    # 3色でグループ分けしたものを、色ごとにグループ分けしたものを、色ごとにグループ分け
    C1_1_1 = []
    C1_1_2 = []
    C1_1_3 = []
    C1_2_1 = []
    C1_2_2 = []
    C1

if __name__ == '__main__':
    main()