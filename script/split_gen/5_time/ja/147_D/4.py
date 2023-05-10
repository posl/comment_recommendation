def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        bit = 0
        for j in range(n):
            if a[j]&(1<<i):
                bit += 1
        ans += bit*(n-bit)*(1<<i)
        ans %= 10**9+7
    print(ans)
