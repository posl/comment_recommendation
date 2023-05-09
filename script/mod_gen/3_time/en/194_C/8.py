def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    sum_sq_a = sum([x*x for x in a])
    ans = 0
    for i in range(n):
        sum_a -= a[i]
        sum_sq_a -= a[i] * a[i]
        ans += sum_sq_a - 2 * a[i] * sum_a
    print(ans)

if __name__ == '__main__':
    main()