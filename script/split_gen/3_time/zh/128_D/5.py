def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k)+1):
        for j in range(min(n, k)-i+1):
            a = v[:i] + v[n-j:]
            a.sort(reverse=True)
            ans = max(ans, sum(a))
    print(ans)
