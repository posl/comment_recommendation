def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    if max(x_list) < min(y_list) and x < min(y_list) and max(x_list) < y:
        print('No War')
    else:
        print('War')

if __name__ == '__main__':
    main()