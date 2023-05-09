def main():
    n, m = map(int, input().split())
    a = [1 for _ in range(n)]
    while True:
        print(*a)
        for i in range(n-1, -1, -1):
            if a[i] < m:
                a[i] += 1
                break
            else:
                a[i] = 1
        else:
            break

if __name__ == '__main__':
    main()