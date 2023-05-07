def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for j in a:
            if j >> i & 1:
                cnt += 1
        ans += cnt * (n - cnt) * 2 ** i
        ans %= 10 ** 9 + 7
    print(ans)
