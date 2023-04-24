Synthesizing 10/10 solutions

=======
Suggestion 1

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

=======
Suggestion 2

def next_permutation(s):
    i = len(s) - 1
    while i > 0 and s[i-1] >= s[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(s) - 1
    while s[j] <= s[i-1]:
        j -= 1
    s[i-1], s[j] = s[j], s[i-1]
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return True

s, k = input().split()
s = list(s)
k = int(k)
for i in range(k):
    next_permutation(s)
print(''.join(s))

=======
Suggestion 3

def permute(s):
    if len(s) == 1:
        return [s]
    else:
        return [s[i] + p for i in range(len(s)) for p in permute(s[:i] + s[i+1:])]

=======
Suggestion 4

def permutations(s):
    if len(s) == 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
            for p in permutations(s[:i] + s[i+1:]):
                res.append(s[i] + p)
        return res

s, k = input().split()
k = int(k)
print(sorted(permutations(s))[k-1])

=======
Suggestion 5

def permute(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            for p in permute(s[:i] + s[i+1:]):
                perms.append(s[i] + p)
        return perms

=======
Suggestion 6

def permute(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            perms += [s[i] + p for p in permute(s[:i] + s[i+1:])]
        return perms

S, K = input().split()
K = int(K)
perms = permute(S)
perms.sort()
print(perms[K-1])

=======
Suggestion 7

def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    for i in range(K-1):
        S = next_permutation(S)
    print(''.join(S))

=======
Suggestion 8

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

=======
Suggestion 9

def permute(s):
    if len(s) == 1:
        return [s]
    else:
        perm = []
        for i in range(len(s)):
            x = s[i]
            xs = s[:i] + s[i+1:]
            for p in permute(xs):
                perm.append(x + p)
        return perm

s, k = input().split()
k = int(k)
perms = permute(s)
perms.sort()
print(perms[k-1])

=======
Suggestion 10

def solve(s,k):
    if len(s) == 1:
        return s
    s = list(s)
    s.sort()
    n = len(s)
    for i in range(n):
        if s[i] != s[0]:
            break
    if i == 1:
        return s[0] + solve(s[1:],k)
    if k <= i * factorial(n-1):
        return s[0] + solve(s[1:],k)
    else:
        return s[i] + solve(s[:i] + s[i+1:],k-i*factorial(n-1))

s,k = input().split()
k = int(k)
print(solve(s,k))
