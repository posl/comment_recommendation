def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if a[i] != x:
            b.append(a[i])
    print(*b)

if __name__ == '__main__':
    main()