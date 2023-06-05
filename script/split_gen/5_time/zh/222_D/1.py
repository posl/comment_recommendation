def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    ans = 1
    for i in range(n):
        ans = ans * (min(b[i], max(a[i], b[i - 1])) - a[i] + 1) % mod
    print(ans)
