def main():
    N, Q = map(int, input().split())
    xs = [int(input()) for _ in range(Q)]
    # 1 2 3 4 5
    # 1 2 4 3 5
    # 1 2 4 5 3
    # 1 2 5 4 3
    # 1 2 3 4 5 6
    # 1 2 3 4 6 5
    # 1 2 3 6 4 5
    # 1 2 6 3 4 5
    # 1 6 2 3 4 5
    # 6 1 2 3 4 5
    # 1 2 3 4 5 6 7
    # 1 2 3 4 5 7 6
    # 1 2 3 4 7 5 6
    # 1 2 3 7 4 5 6
    # 1 2 7 3 4 5 6
    # 1 7 2 3 4 5 6
    # 7 1 2 3 4 5 6
    # 1 2 3 4 5 6 7 8
    # 1 2 3 4 5 6 8 7
    # 1 2 3 4 5 8 6 7
    # 1 2 3 4 8 5 6 7
    # 1 2 3 8 4 5 6 7
    # 1 2 8 3 4 5 6 7
    # 1 8 2 3 4 5 6 7
    # 8 1 2 3 4 5 6 7
    # 1 2 3 4 5 6 7 8 9
    # 1 2 3 4 5 6 7 9 8
    # 1 2 3 4 5 6 9 7