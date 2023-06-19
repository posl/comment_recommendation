def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        a[i] -= 1
        p += a[i] // 4
        a[i] %= 4
        if a[i] == 0:
            continue
        p += 1
        if i < n - 1:
            a[i + 1] -= a[i]
    print(p)

if __name__ == '__main__':
    main()