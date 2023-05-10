def calc(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n % 2 == 0:
        return (calc(n//2)**2) % 998244353
    else:
        return (calc(n//2)**2 * 2) % 998244353
N = int(input())
A = list(map(int, input().split()))
cnt = [0] * 10
for i in range(N):
    cnt[A[i]] += 1
ans = [0] * 10
for i in range(10):
    for j in range(10):
        if (i + j) % 10 == i:
            ans[i] += cnt[i] * cnt[j]
            ans[i] %= 998244353
        if (i * j) % 10 == i:
            ans[i] += cnt[i] * cnt[j]
            ans[i] %= 998244353
for i in range(10):
    print(ans[i])

if __name__ == '__main__':
    calc()