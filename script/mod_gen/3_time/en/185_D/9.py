def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n + 1)
    m += 1
    if m == 1:
        print(1)
        return
    diff = []
    for i in range(1, m):
        if a[i] - a[i - 1] > 1:
            diff.append(a[i] - a[i - 1] - 1)
    if len(diff) == 0:
        print(0)
        return
    k = min(diff)
    ans = 0
    for d in diff:
        ans += (d + k - 1) // k
    print(ans)

if __name__ == '__main__':
    main()