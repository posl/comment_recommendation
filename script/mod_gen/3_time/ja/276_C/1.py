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
n = int(input())
p = list(map(int, input().split()))
q = list(range(1, n + 1))
k = int(input())
for i in range(k):
    next_permutation(q)
print(*q)

if __name__ == '__main__':
    next_permutation()