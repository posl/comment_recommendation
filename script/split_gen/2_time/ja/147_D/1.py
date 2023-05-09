def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        cnt = 0
        for a in A:
            if (a >> i) & 1:
                cnt += 1
        ans += cnt * (N - cnt) * pow(2, i, 10 ** 9 + 7)
        ans %= 10 ** 9 + 7
    print(ans)
