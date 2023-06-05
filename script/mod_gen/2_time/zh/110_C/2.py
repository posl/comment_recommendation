def main():
    n, m, x, y = map(int, input().split())
    x = x + 1
    y = y - 1
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)
    x_list.sort()
    y_list.sort()
    if x_list[-1] > y_list[0]:
        print('War')
    else:
        print('No War')

if __name__ == '__main__':
    main()