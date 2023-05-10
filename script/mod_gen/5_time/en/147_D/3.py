def xor_sum(n, a):
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        ans += (cnt * (n - cnt) * (1 << i))
        ans %= 1000000007
    return ans
n = int(input())
a = list(map(int, input().split()))
print(xor_sum(n, a))

if __name__ == '__main__':
    xor_sum()