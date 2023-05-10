def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    max_bit = 1
    for i in range(1, 41):
        if k < max_bit:
            break
        max_bit *= 2
    max_bit //= 2
    bit = 0
    ans = 0
    while max_bit > 0:
        count = 0
        for i in range(n):
            if a[i] & max_bit:
                count += 1
        if count < n - count and bit + max_bit <= k:
            bit += max_bit
        ans += max_bit * (n - count if count < n - count else count)
        max_bit //= 2
    print(ans)
