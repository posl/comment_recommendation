def base_k_to_base_10(k, a):
    base_10 = 0
    for i in range(len(a)):
        base_10 += int(a[i]) * pow(k, len(a) - i - 1)
    return base_10
k = int(input())
a, b = map(str, input().split())
a_base_10 = base_k_to_base_10(k, a)
b_base_10 = base_k_to_base_10(k, b)
print(a_base_10 * b_base_10)
