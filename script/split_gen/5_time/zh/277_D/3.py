def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    ans = 0
    for i in range(1, n+1):
        if a[i] != a[i-1]:
            ans += a[i] - a[i-1] - 1
    print(ans)
