def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    mod = 998244353
    ans = 1
    for i in range(n):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= mod
    print(ans)
