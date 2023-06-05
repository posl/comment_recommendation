def get_next_permutation(a):
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
n = int(input())
p = list(map(int, input().split()))
p1 = p[:]
p2 = p[:]
get_next_permutation(p1)
get_next_permutation(p2)
for i in range(n):
    if p1[i] != p2[i]:
        print(*p1)
        exit()
print(-1)
