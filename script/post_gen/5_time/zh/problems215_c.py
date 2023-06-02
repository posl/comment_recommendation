Synthesizing 10/10 solutions

=======
Suggestion 1

def permutation(lst):
    if len(lst) <= 1:
        return [lst]
    r = []
    for i in range(len(lst)):
        s = lst[:i] + lst[i+1:]
        p = permutation(s)
        for x in p:
            r.append(lst[i:i+1] + x)
    return r

=======
Suggestion 2

def get_permutations(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i in range(len(s)):
            for j in get_permutations(s[:i]+s[i+1:]):
                result.append(s[i]+j)
        return result

=======
Suggestion 3

def get_permutation(s, k):
    s = list(s)
    s.sort()
    k = k - 1
    result = []
    for i in range(len(s) - 1, -1, -1):
        j = k // factorial(i)
        k = k % factorial(i)
        result.append(s[j])
        del s[j]
    return ''.join(result)

=======
Suggestion 4

def next_permutation(a):
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i+1]:
        i -= 1
    if i == -1:
        return False
    j = len(a) - 1
    while a[i] >= a[j]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i+1:] = reversed(a[i+1:])
    return True

=======
Suggestion 5

def get_permutation(s, k):
    from itertools import permutations
    perm = sorted(set(permutations(s)))
    if k > len(perm):
        return 'None'
    else:
        return ''.join(perm[k-1])

=======
Suggestion 6

def next_permutation(a):
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i + 1]):
        i -= 1
    if i < 0:
        return False
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

=======
Suggestion 7

def permutation(s):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in permutation(s[:i] + s[i+1:]):
            sl.append(s[i] + j)
    return sl

=======
Suggestion 8

def get_permutations(s):
    if len(s) == 1:
        return [s]
    else:
        perm_list = []
        for i in range(len(s)):
            for perm in get_permutations(s[:i] + s[i+1:]):
                perm_list.append(s[i] + perm)
        return perm_list

=======
Suggestion 9

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 10

def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
            for j in permutation(s[:i] + s[i+1:]):
                res.append(s[i] + j)
        return res
