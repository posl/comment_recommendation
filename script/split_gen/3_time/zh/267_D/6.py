def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-m+1):
        ans = max(ans, sum([(i+1)*a[i] for i in range(i, i+m)]))
    print(ans)
