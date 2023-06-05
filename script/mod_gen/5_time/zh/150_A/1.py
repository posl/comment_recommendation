def main():
    K, X = map(int, input().split())
    if K * 500 >= X:
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()