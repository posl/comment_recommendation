def main():
    # H, W, C = map(int, input().split())
    # A = [list(map(int, input().split())) for _ in range(H)]
    H, W, C = 3, 3, 1000000000
    A = [[1000000, 1000000, 1], [1000000, 1000000, 1000000], [1, 1000000, 1000000]]
    print(H, W, C)
    print(A)
    # 1行目、1列目、2列目の最小値を求める
    min_1_1 = min(A[0][0], A[0][1], A[1][0])
    min_1_2 = min(A[0][1], A[0][2], A[1][2])
    min_2_1 = min(A[1][0], A[2][0], A[2][1])
    print(min_1_1, min_1_2, min_2_1)
    min_1 = min(min_1_1, min_1_2)
    min_2 = min(min_1_1, min_2_1)
    min_3 = min(min_1_2, min_2_1)
    print(min_1, min_2, min_3)
    # 1行目、1列目、2列目の最小値を求める
    min_1_1 = min(A[0][0], A[0][1], A[1][0])
    min_1_2 = min(A[0][1], A[0][2], A[1][2])
    min_2_1 = min(A[1][0], A[2][0], A[2][1])
    print(min_1_1, min_1_2, min_2_1)
    min_1 = min(min_1_1, min_1_2)
    min_2 = min(min_1_1, min_2_1)
    min_3 = min(min_1_2, min_2_1)
    print(min_1, min_2, min_3)

if __name__ == '__main__':
    main()