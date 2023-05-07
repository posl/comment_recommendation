def xor_sum(n, a):
    sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            sum += a[i] ^ a[j]
    return sum
n = int(input())
a = [int(x) for x in input().split()]
print(xor_sum(n, a) % (10**9 + 7))
