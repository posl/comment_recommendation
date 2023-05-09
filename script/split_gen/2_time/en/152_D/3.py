def main():
    N = int(input())
    cnt = [0] * 10
    for i in range(1, N + 1):
        cnt[i % 10] += 1
    ans = 0
    for i in range(1, N + 1):
        ans += cnt[i // 10 % 10] * cnt[i % 10]
    print(ans)
