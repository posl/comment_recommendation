def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        c = 0
        for j in range(n):
            if a[j] & (1 << i):
                c += 1
        ans += c * (n - c) * (1 << i)
        ans %= (10 ** 9 + 7)
    print(ans)
