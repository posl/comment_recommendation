def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = float('inf')
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                p = sum(a[:i])
                q = sum(a[i:j])
                r = sum(a[j:k])
                s = sum(a[k:])
                ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)
main()
