def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = {}
    for i in range(n):
        c[a[i]] = c.get(a[i], 0) + 1
    ans = [0 for i in range(n)]
    for i in range(n):
        ans[i] = c[a[i]] * (c[a[i]] - 1) // 2
    total = sum(ans)
    for i in range(n):
        print(total - ans[a[i]] + 1)
