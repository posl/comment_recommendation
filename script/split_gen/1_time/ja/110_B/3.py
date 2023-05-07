def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x_max = max(x)
    y_min = min(y)
    if x_max < y_min and X < y_min <= Y:
        print('No War')
    else:
        print('War')
