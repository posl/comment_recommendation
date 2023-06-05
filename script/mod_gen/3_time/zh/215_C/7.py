def next_permutation(a):
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = len(a) - 1
    while a[i] >= a[j]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = a[i + 1:][::-1]
    return True
s, k = input().split()
k = int(k)
a = sorted(s)
for i in range(k - 1):
    next_permutation(a)
print(''.join(a))

if __name__ == '__main__':
    next_permutation()