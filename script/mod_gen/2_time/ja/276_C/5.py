def nextPermutation(a):
    # 1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    k = -1
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            k = i
    if k == -1:
        return False
    # 2. Find the largest index l greater than k such that a[k] < a[l].
    l = -1
    for i in range(k + 1, len(a)):
        if a[k] < a[i]:
            l = i
    if l == -1:
        return False
    # 3. Swap the value of a[k] with that of a[l].
    a[k], a[l] = a[l], a[k]
    # 4. Reverse the sequence from a[k + 1] up to and including the final element a[n].
    a[k + 1:] = a[len(a) - 1:k:-1]
    return True
n = int(input())
p = list(map(int, input().split()))
a = list(range(1, n + 1))
ans = []
for i in range(n):
    for j in range(1, n + 1):
        a[i], a[j] = a[j], a[i]
        if a == p:
            ans = a[:]
        a[i], a[j] = a[j], a[i]
print(*ans)

if __name__ == '__main__':
    nextPermutation()