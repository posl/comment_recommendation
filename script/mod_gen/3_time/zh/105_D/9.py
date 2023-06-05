def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    sum_a = [0] * (n + 1)
    for i in range(n):
        sum_a[i + 1] = sum_a[i] + a[i]
        sum_a[i + 1] %= m
    from collections import Counter
    c = Counter(sum_a)
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()