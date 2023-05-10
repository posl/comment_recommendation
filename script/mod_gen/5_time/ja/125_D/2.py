def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    minus = 0
    min_minus = 10**9
    for i in range(n):
        if a[i] < 0:
            minus += 1
            if min_minus > -a[i]:
                min_minus = -a[i]
        ans += abs(a[i])
    if minus % 2 == 1:
        ans -= 2 * min_minus
    print(ans)

if __name__ == '__main__':
    main()