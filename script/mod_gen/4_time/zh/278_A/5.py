def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[k:] + [0] * k
    print(*a)

if __name__ == '__main__':
    main()