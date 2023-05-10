def main():
    n, q = map(int, input().split())
    a = [0] * n
    for i in range(n - 1):
        x, y = map(int, input().split())
        a[x - 1] += 1
        a[y - 1] += 1
    for i in range(q):
        x, y = map(int, input().split())
        a[x - 1] += y
    print(*a)

if __name__ == '__main__':
    main()