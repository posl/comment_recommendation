def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = n
    for i in range(m):
        ans -= a[i]
    print(-1 if ans < 0 else ans)
