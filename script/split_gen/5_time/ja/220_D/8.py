def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 10
    for i in a:
        cnt[i] += 1
    ans = [0] * 10
    ans[0] = (cnt[0] * cnt[0] * cnt[0] * cnt[0] * cnt[0]) % 998244353
    for i in range(1, 10):
        if cnt[i] == 0:
            continue
        for j in range(10):
            if cnt[j] == 0:
                continue
            ans[(i * j) % 10] += cnt[i] * cnt[j]
            ans[(i * j) % 10] %= 998244353
    for i in ans:
        print(i)
