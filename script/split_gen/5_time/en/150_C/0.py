def next_permutation(a):
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        return False
    j = len(a) - 1
    while not (a[i] < a[j]):
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i+1:] = reversed(a[i+1:])
    return True
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
a = 0
b = 0
i = 0
while i < n:
    a += p[i] * (n ** i)
    b += q[i] * (n ** i)
    i += 1
print(abs(a - b))
