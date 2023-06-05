def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    x_max = x[N-1]
    y_min = y[0]
    if x_max >= y_min:
        print("War")
    else:
        if X < x_max < Y and X < y_min < Y:
            print("No War")
        else:
            print("War")
