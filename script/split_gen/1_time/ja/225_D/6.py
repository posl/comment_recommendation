def main():
    n, q = map(int, input().split())
    # 電車の番号を格納するリスト
    trains = [i for i in range(1, n+1)]
    # 電車の番号と電車の前後を格納するリスト
    # 例：[1, 2, 3, 4, 5, 6, 7]
    #     [0, 1, 2, 3, 4, 5, 6]
    #     [1, 2, 3, 4, 5, 6, 0]
    #     [1, 2, 3, 4, 5, 0, 6]
    #     [1, 2, 3, 4, 0, 5, 6]
    #     [1, 2, 3, 0, 4, 5, 6]
    #     [1, 2, 0, 3, 4, 5, 6]
    #     [1, 0, 2, 3, 4, 5, 6]
    #     [0, 1, 2, 3, 4, 5, 6]
    #     [1, 2, 3, 4, 5, 6, 0]
    #     [1, 5, 2, 3, 4, 0, 6]
    #     [1, 5, 2, 3, 4, 6, 0]
    #     [1, 5, 2, 3, 0, 4, 6]
    #     [1, 5, 2, 0, 3, 4, 6]
    #     [1, 5, 0, 2, 3, 4, 6]
    #     [1, 0, 5, 2, 3, 4, 6]
    #     [0, 1, 5, 2, 3, 4, 6]
    #     [1, 5, 2,
