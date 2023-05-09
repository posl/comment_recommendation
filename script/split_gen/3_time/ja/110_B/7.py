def main():
    # N, M, X, Y = map(int, input().split())
    # x = list(map(int, input().split()))
    # y = list(map(int, input().split()))
    N, M, X, Y = 3, 2, 10, 20
    x = [8, 15, 13]
    y = [16, 22]
    # N, M, X, Y = 4, 2, -48, -1
    # x = [-20, -35, -91, -23]
    # y = [-22, 66]
    # N, M, X, Y = 5, 3, 6, 8
    # x = [-10, 3, 1, 5, -100]
    # y = [100, 6, 14]
    if X < Y:
        if max(x) < min(y) and X < min(y) and min(y) <= Y:
            print('No War')
        else:
            print('War')
    else:
        print('War')
