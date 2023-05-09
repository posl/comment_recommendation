def xor_sum(n, a):
    ans = 0
    for i in range(60):
        count = 0
        for j in range(n):
            if a[j] & (1 << i):
                count += 1
        ans += (count * (n - count) * (1 << i)) % (10**9+7)
    return ans % (10**9+7)
n = int(input())
a = list(map(int, input().split()))
print(xor_sum(n, a))
