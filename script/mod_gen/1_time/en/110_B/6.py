def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # print(N, M, X, Y)
    # print(x)
    # print(y)
    x_max = max(x)
    y_min = min(y)
    # print(x_max)
    # print(y_min)
    for z in range(X+1, Y+1):
        # print(z)
        if x_max < z <= y_min:
            print('No War')
            break
    else:
        print('War')

if __name__ == '__main__':
    main()