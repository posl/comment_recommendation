def main():
    n, k = map(int, input().split())
    ans = 0
    for a in range(1, n + 1):
        if a % k == 0:
            ans += n // k
        else:
            ans += n // k + 1
    if k % 2 == 0:
        for b in range(1, n + 1):
            if (b + k // 2) % k == 0:
                ans += n // k
            else:
                ans += n // k + 1
    if k % 3 == 0:
        for c in range(1, n + 1):
            if (c + k // 3) % k == 0:
                ans += n // k
            else:
                ans += n // k + 1
    if k % 6 == 0:
        for d in range(1, n + 1):
            if (d + k // 6) % k == 0:
                ans += n // k
            else:
                ans += n // k + 1
    print(ans)

if __name__ == '__main__':
    main()