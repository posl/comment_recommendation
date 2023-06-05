def get_next_permutation(a):
    n = len(a)
    i = n - 1
    while a[i - 1] >= a[i]:
        i -= 1
    j = n - 1
    while j >= i and a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    a[i:] = a[n - 1: i - 1: -1]
    return a
n = int(input())
p = list(map(int, input().split()))
q = get_next_permutation(p)
print(*q)
