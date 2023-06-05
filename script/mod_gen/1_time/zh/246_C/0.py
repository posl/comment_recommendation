def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n):
        if k > 0:
            res += max(a[i] - x, 0)
            k -= 1
        else:
            res += a[i]
    print(res)

if __name__ == '__main__':
    main()