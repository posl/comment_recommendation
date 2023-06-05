Synthesizing 10/10 solutions

=======
Suggestion 1

def permutation(s, k):
    if len(s) == 1:
        return s
    n = len(s)
    c = 1
    for i in range(1, n):
        c *= i
    q = int((k - 1) / c)
    r = k - c * q
    return s[q] + permutation(s[:q] + s[q+1:], r)

=======
Suggestion 2

def permutation(s):
    if len(s) <=1:
        yield s
    else:
        for i in range(len(s)):
            for j in permutation(s[:i] + s[i+1:]):
                yield s[i] + j

=======
Suggestion 3

def getPermutation(s, k):
    if len(s) == 1:
        return s
    else:
        char_list = list(s)
        char_list.sort()
        next_str = ''.join(char_list[1:])
        num = 1
        for i in range(1, len(s)):
            num *= i
        index = (k - 1) / num
        return char_list[index] + getPermutation(next_str, k - index * num)

=======
Suggestion 4

def next_permutation(a):
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = len(a) - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

S, K = input().split()
S = sorted(S)
K = int(K)
for _ in range(K - 1):
    next_permutation(S)
print(''.join(S))

=======
Suggestion 5

def next_permutation(a):
    # Find non-increasing suffix
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    
    # Reverse suffix
    a[i : ] = a[len(a) - 1 : i - 1 : -1]
    return True

=======
Suggestion 6

def get_permutation(s, k):
    if len(s) == 1:
        return s
    else:
        l = list(s)
        l.sort()
        s = ''.join(l)
        n = len(s)
        if k == 1:
            return s
        elif k == 2:
            return s[::-1]
        else:
            if k == factorial(n):
                return s[::-1]
            else:
                t = factorial(n-1)
                p = k / t
                q = k % t
                if q == 0:
                    q = t
                return s[p-1] + get_permutation(s[:p-1] + s[p:], q)

=======
Suggestion 7

def permutation(S):
    if len(S) == 1:
        return [S]
    else:
        res = []
        for i in range(len(S)):
            res += [S[i] + x for x in permutation(S[:i] + S[i+1:])]
        return res

=======
Suggestion 8

def get_permutation(s, n, k):
    if n == 1:
        return s
    q, r = divmod(k, factorial(n - 1))
    return s[q] + get_permutation(s[:q] + s[q + 1:], n - 1, r)

=======
Suggestion 9

def getPermutation(s, k):
    if len(s) == 1:
        return s
    else:
        s = sorted(s)
        n = len(s)
        f = [1]
        for i in range(1, n):
            f.append(f[i-1] * i)
        if k > f[n-1] * n:
            return "Error"
        else:
            for i in range(n):
                if k <= f[n-1]:
                    return s[0] + getPermutation(s[1:], k)
                else:
                    k -= f[n-1]
                    s = s[1:]

=======
Suggestion 10

def get_permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for i, c in enumerate(s):
            for perm in get_permutations(s[:i] + s[i+1:]):
                perms.append(c + perm)
    return perms
