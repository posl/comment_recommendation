def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = [0]
    for i in range(n):
        sum_a.append(sum_a[-1] + a[i])
    ans = - 2 * 10**5 * n
    for i in range(n - m + 1):
        ans = max(ans, sum_a[i + m] - sum_a[i])
    print(ans)

if __name__ == '__main__':
    main()