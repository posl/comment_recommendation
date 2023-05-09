def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = [0] * (n + 1)
    ans[0] = 1
    for i in range(n + 1):
        if ans[i] == 0:
            continue
        for j in range(m):
            if i + a[j] <= n:
                ans[i + a[j]] = max(ans[i + a[j]], ans[i] * 10 + a[j])
    print(ans[n])
