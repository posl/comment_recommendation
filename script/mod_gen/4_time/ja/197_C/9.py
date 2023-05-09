def check_bit(x):
    bit = 0
    for i in range(30):
        if (x >> i) & 1:
            bit |= (1 << i)
    return bit
n = int(input())
a = list(map(int, input().split()))
ans = 1 << 30
for i in range(n):
    bit = 0
    for j in range(i, n):
        bit |= a[j]
        if bit == (1 << 30) - 1:
            ans = min(ans, check_bit(bit))
            break
        if j == n - 1:
            ans = min(ans, check_bit(bit))
print(ans)

if __name__ == '__main__':
    check_bit()