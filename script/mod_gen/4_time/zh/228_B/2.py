def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    a = set(a)
    print(len(a))

if __name__ == '__main__':
    main()