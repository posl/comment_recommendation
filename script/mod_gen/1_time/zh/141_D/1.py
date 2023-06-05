def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    i = 0
    while m > 0:
        a[i] = a[i] // 2
        m -= 1
        i += 1
        if i == n:
            i = 0
    print(sum(a))

if __name__ == '__main__':
    main()