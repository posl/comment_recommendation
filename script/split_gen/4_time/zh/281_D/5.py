def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = -1
    for i in range(n-k+1):
        if a[i]%d == 0:
            ans = max(ans, sum(a[i:i+k]))
    print(ans)
