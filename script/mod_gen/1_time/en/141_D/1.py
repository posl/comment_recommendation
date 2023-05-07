def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        a[0] = a[0] // 2
        a.sort()
    print(sum(a))

if __name__ == '__main__':
    main()