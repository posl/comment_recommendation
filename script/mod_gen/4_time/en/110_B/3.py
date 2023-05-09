def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x_max = max(x)
    y_min = min(y)
    z = x_max + 1
    if z > y_min:
        print('War')
    elif z <= X or z > Y:
        print('War')
    else:
        print('No War')

if __name__ == '__main__':
    main()