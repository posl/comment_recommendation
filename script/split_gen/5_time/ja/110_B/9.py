def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)
    if max(x_list) >= min(y_list):
        print('War')
    else:
        print('No War')
