def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    if n == k-1:
        print(1)
        return
    elif n < k-1:
        print(0)
        return
    else:
        ans = 0
        for i in range(k, n+2):
            min = i*(i-1)//2
            max = i*(2*n-i+1)//2
            ans += max-min+1
            ans %= mod
        print(ans)
