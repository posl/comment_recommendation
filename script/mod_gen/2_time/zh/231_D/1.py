def main():
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(m):
        x, y = map(int, input().split())
        a[x] += 1
        a[y] += 1
    for i in range(1, n + 1):
        if a[i] % 2 == 1:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()