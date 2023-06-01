Synthesizing 10/10 solutions

=======
Suggestion 1

def permutation(string):
    if len(string) <= 1:
        return [string]
    else:
        result = []
        for i in range(len(string)):
            for j in permutation(string[:i] + string[i+1:]):
                result.append(string[i] + j)
    return result

=======
Suggestion 2

def getPermutation(s, k):
    if len(s) == 1:
        return s
    else:
        s = sorted(s)
        for i in range(len(s)):
            if k <= factorial(len(s) - 1):
                return s[i] + getPermutation(s[:i] + s[i+1:], k)
            else:
                k -= factorial(len(s) - 1)
        return s[0] + getPermutation(s[1:], k)

=======
Suggestion 3

def permutate(s):
    if len(s) == 1:
        return [s]
    elif len(s) == 2:
        return [s, s[1] + s[0]]
    else:
        result = []
        for i in range(len(s)):
            for j in permutate(s[:i] + s[i + 1:]):
                result.append(s[i] + j)
        return result

=======
Suggestion 4

def next_permutation(a):
    """Generate the lexicographically next permutation inplace.
    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.py
    Return false if there is no next permutation.
    """
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
Suggestion 5

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
    a[i : ] = a[n - 1 : i - 1 : -1]
    return True

=======
Suggestion 6

def findKthPermutation(s, k):
    if k == 1:
        return s
    length = len(s)
    if length == 1:
        return s
    #计算阶乘
    factorial = 1
    for i in range(1, length):
        factorial *= i
    #计算当前位
    quotient = k / factorial
    remainder = k % factorial
    if remainder == 0:
        quotient -= 1
        remainder = factorial
    #取当前位
    current_char = s[quotient]
    #取剩余字符串
    rest = s[:quotient] + s[quotient + 1:]
    #递归
    return current_char + findKthPermutation(rest, remainder)

=======
Suggestion 7

def getPermutation(s, k):
    s = list(s)
    s.sort()
    return dfs(s, k, 0, len(s))

=======
Suggestion 8

def getPermutation(s, k):
    if len(s) == 1:
        return s
    else:
        n = len(s)
        a = 1
        for i in range(n):
            a *= (i + 1)
        b = a / n
        c = k / b
        d = k % b
        if d == 0:
            c -= 1
            d = b
        return s[c] + getPermutation(s[0:c] + s[c + 1:n], d)

=======
Suggestion 9

def swap(s, i, j):
    if i == j:
        return s
    if i > j:
        i, j = j, i
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

=======
Suggestion 10

def permutation(string, s, e):
    if s == e:
        return [string]
    else:
        res = []
        for i in range(s, e):
            string[s], string[i] = string[i], string[s]
            res += permutation(string, s+1, e)
            string[s], string[i] = string[i], string[s]
        return res
