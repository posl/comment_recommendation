def k_to_10(k, n):
    k = int(k)
    n = str(n)
    l = len(n)
    ans = 0
    for i in range(l):
        ans += int(n[i]) * (k ** (l - i - 1))
    return ans
k = input()
a, b = map(str, input().split())
print(k_to_10(k, a) * k_to_10(k, b))
