def main():
    n = int(input())
    print('1', end=' ')
    for i in range(2, n+1):
        print(i, end=' ')
        print('1', end=' ')
        for j in range(2, i+1):
            print(j, end=' ')
            print('1', end=' ')
    print('')

if __name__ == '__main__':
    main()