def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    sum_a2 = sum([i**2 for i in a])
    ans = 0
    for i in range(n):
        sum_a -= a[i]
        sum_a2 -= a[i]**2
        ans += (n - 1 - i) * a[i]**2 + 2 * a[i] * sum_a - sum_a2
    print(ans)

if __name__ == '__main__':
    main()