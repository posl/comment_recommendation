def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) - i + 1):
            tmp = v[:i] + v[n - j:]
            tmp.sort()
            ans = max(ans, sum(tmp[max(0, k - i - j):]))
    print(ans)
