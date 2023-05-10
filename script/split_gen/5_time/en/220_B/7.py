def base_k_to_10(n, k):
    res = 0
    for i in range(len(n)):
        res += int(n[i]) * (k ** (len(n)-1-i))
    return res
k = int(input())
a, b = input().split()
print(base_k_to_10(a, k) * base_k_to_10(b, k))
