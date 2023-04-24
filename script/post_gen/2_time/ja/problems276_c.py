Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

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

=======
Suggestion 2

def next_permutation(a):
    n = len(a)
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = a[n - 1:i:-1]
    return True

=======
Suggestion 3

def next_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i - 1] >= seq[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(seq) - 1
    while seq[j] <= seq[i - 1]:
        j -= 1
    seq[i - 1], seq[j] = seq[j], seq[i - 1]
    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
    return True

=======
Suggestion 4

def next_permutation(A):
    N = len(A)
    i = N - 1
    while i > 0 and A[i - 1] >= A[i]:
        i -= 1
    if i == 0:
        return False
    j = N - 1
    while A[j] <= A[i - 1]:
        j -= 1
    A[i - 1], A[j] = A[j], A[i - 1]
    j = N - 1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return True

=======
Suggestion 5

def next_permutation(a):
    l = len(a)
    i = l - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = l - 1
    while a[i] >= a[j]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

=======
Suggestion 6

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

=======
Suggestion 7

def next_permutation(L):
    if len(L) == 1:
        return False
    i = len(L) - 1
    while i > 0 and L[i-1] >= L[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(L) - 1
    while L[j] <= L[i-1]:
        j -= 1
    L[i-1], L[j] = L[j], L[i-1]
    j = len(L) - 1
    while i < j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1
    return True

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [i-1 for i in p]
    #print(p)
    a = [i for i in range(n)]
    #print(a)
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
                a[i], a[j] = a[j], a[i]
    for i in range(n):
        print(a[i] + 1, end=' ')
    print()
