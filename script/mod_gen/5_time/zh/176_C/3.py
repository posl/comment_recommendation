def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 从前往后遍历，如果当前值比前一个值高，那么当前值的凳子高度要比前一个值的凳子高度高1
    # 如果当前值比前一个值低，那么当前值的凳子高度要比前一个值的凳子高度低到能满足条件为止
    ans = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            ans += a[i] - a[i-1]
        elif a[i] < a[i-1]:
            ans -= a[i-1] - a[i]
            if ans < 0:
                ans = 0
    print(ans)

if __name__ == '__main__':
    main()