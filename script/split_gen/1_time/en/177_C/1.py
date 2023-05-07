def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += a[i] * sum(a[i+1:])
    print(ans % (10**9+7))
