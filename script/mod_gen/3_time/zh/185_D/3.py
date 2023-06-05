def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if m == 0:
        print(1)
        return
    a.sort()
    a.append(n + 1)
    ans = n
    start = 0
    for i in range(m + 1):
        if a[i] - start - 1 > 0:
            ans = min(ans, a[i] - start - 1)
        start = a[i] + 1
    print(ans)

if __name__ == '__main__':
    main()