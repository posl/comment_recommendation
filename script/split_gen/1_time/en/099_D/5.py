def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            c[i][j] -= 1
    # print(N, C)
    # print(D)
    # print(c)
    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9
    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9
    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9
    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9
    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9
    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9
    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9
    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9
    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9
    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9
    # 1, 2, 3
    # 4, 5, 6
    # 7, 8, 9
    # 1, 4, 7
    # 2, 5, 8
    # 3, 6, 9
    # 1, 2, 3
    #
