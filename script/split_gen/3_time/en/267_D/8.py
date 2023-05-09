def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            b = a[i:j+1]
            b.sort()
            ans = max(ans, sum(b[-m:]))
    print(ans)
