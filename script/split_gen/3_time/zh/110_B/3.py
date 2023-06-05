def main():
    # N, M, X, Y = map(int, input().split())
    # x = list(map(int, input().split()))
    # y = list(map(int, input().split()))
    N, M, X, Y = 3, 2, 10, 20
    x = [8, 15, 13]
    y = [16, 22]
    x.sort()
    y.sort()
    if x[-1] < y[0] and X < y[0] and y[0] <= Y:
        print("No War")
    else:
        print("War")
