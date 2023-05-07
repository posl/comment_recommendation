def next_permutation(a):
    n = len(a)
    i = n - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = n - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = n - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True
N = int(input())
P = list(map(int,input().split()))
count = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if P[i-1] > P[j-1]:
            count += 1
