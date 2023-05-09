def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_max = max(x_list)
    y_min = min(y_list)
    if x_max < y_min and x < y_min and x_max < y:
        print('No War')
    else:
        print('War')
