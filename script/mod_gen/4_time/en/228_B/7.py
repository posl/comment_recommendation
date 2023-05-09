def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    print(a.count(1))

if __name__ == '__main__':
    main()