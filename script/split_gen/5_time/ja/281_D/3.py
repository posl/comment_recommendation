def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = -1
    if n >= k:
        for i in range(n-k+1):
            if a[i] % d == 0:
                ans = a[i]
                break
    print(ans)
