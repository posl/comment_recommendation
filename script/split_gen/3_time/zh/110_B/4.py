def input():
    N, M, X, Y = input().split()
    N, M, X, Y = int(N), int(M), int(X), int(Y)
    x_list = [int(x) for x in input().split()]
    y_list = [int(y) for y in input().split()]
    return N, M, X, Y, x_list, y_list
