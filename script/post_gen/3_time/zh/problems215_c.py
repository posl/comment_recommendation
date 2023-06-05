Synthesizing 10/10 solutions

=======
Suggestion 1

def get_permutations(string):
    if len(string) == 1:
        return [string]
    else:
        res = []
        for i in range(len(string)):
            for j in get_permutations(string[:i] + string[i+1:]):
                res.append(string[i] + j)
        return res

=======
Suggestion 2

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 3

def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        result = []
        for i, c in enumerate(s):
            result += [c + p for p in permutation(s[:i] + s[i+1:])]
        return result

=======
Suggestion 4

def permutation(string, start, end):
    if start == end:
        print(''.join(string))
        return

    for i in range(start, end):
        string[start], string[i] = string[i], string[start]
        permutation(string, start+1, end)
        string[start], string[i] = string[i], string[start]

=======
Suggestion 5

def permute(a, k):
    if len(a) == 1:
        return a
    else:
        ret = []
        for i in range(len(a)):
            c = a[i]
            s = a[:i] + a[i+1:]
            p = permute(s, k)
            for x in p:
                ret.append(c + x)
        return ret[k-1]

=======
Suggestion 6

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 7

def permutations(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for j in permutations(s[:i] + s[i+1:]):
                yield s[i] + j

=======
Suggestion 8

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

=======
Suggestion 9

def get_permutation(s, k):
    if len(s) == 1:
        return s
    else:
        s = sorted(s)
        # print(s)
        n = len(s)
        # print(n)
        # print(k)
        if k == 1:
            return s[0] + get_permutation(s[1:], k)
        elif k == n:
            return s[-1] + get_permutation(s[:-1], k-1)
        else:
            if k % factorial(n-1) == 0:
                return s[k//factorial(n-1)-1] + get_permutation(s[:k//factorial(n-1)-1]+s[k//factorial(n-1):], n-1)
            else:
                return s[k//factorial(n-1)] + get_permutation(s[:k//factorial(n-1)]+s[k//factorial(n-1)+1:], k%factorial(n-1))

=======
Suggestion 10

def get_permutation(S, K):
    # print(S, K)
    if len(S) == 1:
        return S
    else:
        n = len(S)
        p = 1
        for i in range(1, n):
            p *= i
        q = K // p
        r = K % p
        if r == 0:
            q -= 1
            r = p
        return S[q] + get_permutation(S[:q] + S[q + 1:], r)
