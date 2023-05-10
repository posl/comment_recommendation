def main():
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(X)
    y_list.append(Y)
    x_max = max(x_list)
    y_min = min(y_list)
    if x_max < y_min:
        print('No War')
    else:
        print('War')

if __name__ == '__main__':
    main()