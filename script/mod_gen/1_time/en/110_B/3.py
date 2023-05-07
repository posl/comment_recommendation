def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y):
        if max(x) < X and min(y) > Y:
            print('War')
        else:
            print('No War')
    else:
        print('War')

if __name__ == '__main__':
    main()