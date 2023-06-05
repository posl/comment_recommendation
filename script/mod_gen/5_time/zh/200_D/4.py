def main():
    n = int(input())
    a = list(map(int,input().split()))
    if n == 2:
        if a[0] % 200 == a[1] % 200:
            print('Yes')
            print('1 1')
            print('1 2')
        else:
            print('No')
    else:
        print('Yes')
        print('1 1')
        print('1 2')

if __name__ == '__main__':
    main()