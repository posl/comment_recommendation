def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    ans = [0] * n
    for i in range(n):
        ans[i] = d[a[i]] * (d[a[i]] - 1) // 2
    for i in range(n):
        print(sum(ans) - (d[a[i]] - 1))

if __name__ == '__main__':
    main()