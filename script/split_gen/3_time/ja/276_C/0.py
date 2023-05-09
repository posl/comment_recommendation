def next_permutation(a):
    n = len(a)
    i = n - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = n - 1
    while a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    j = n - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True
N = int(input())
P = list(map(int, input().split()))
Q = list(range(1, N + 1))
count = 0
while Q != P:
    next_permutation(Q)
    count += 1
print(*Q)
