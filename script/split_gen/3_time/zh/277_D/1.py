def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    ans = 0
    for i in range(n):
        ans += a[i]
    print(ans)
