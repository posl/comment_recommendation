def main():
    n, x = map(int, input().split())
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(n):
        print(a[x // n], end='')
        x = x % n
    print()

if __name__ == '__main__':
    main()