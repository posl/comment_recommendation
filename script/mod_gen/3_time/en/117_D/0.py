def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        c = 0
        for j in a:
            if j >> i & 1:
                c += 1
        if c * 2 < n:
            ans += 1 << i
            c = n - c
        if ans + (1 << i) - 1 <= k:
            ans += (1 << i) * c
    print(ans)

if __name__ == '__main__':
    main()