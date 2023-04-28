Synthesizing 10/10 solutions

=======
Suggestion 1

def permute(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for p in permute(s[:i] + s[i+1:]):
                yield s[i] + p

s, k = input().split()
k = int(k)
s = sorted(list(set(permute(s))))
print(s[k-1])

=======
Suggestion 2

def permutation(string):
    if len(string) == 1:
        return [string]
    else:
        perm_list = []
        for a in string:
            remaining_elements = [x for x in string if x != a]
            z = permutation(remaining_elements)
            for t in z:
                perm_list.append([a] + t)
        return perm_list
#
#def permutation(string):
#    if len(string) == 1:
#        return [string]
#    else:
#        perm_list = []
#        for a in string:
#            remaining_elements = [x for x in string if x != a]
#            z = permutation(remaining_elements)
#            for t in z:
#                perm_list.append([a] + t)
#        return perm_list

=======
Suggestion 3

def permutation(s):
    if len(s) == 1:
        return [s]
    elif len(s) == 2:
        return [s, s[::-1]]
    else:
        l = []
        for i in range(len(s)):
            p = permutation(s[:i] + s[i + 1:])
            for x in p:
                l.append(s[i] + x)
        return l

S, K = input().split()
K = int(K)
S = list(S)
S.sort()
S = "".join(S)

p = permutation(S)
p = list(set(p))
p.sort()
print(p[K - 1])

=======
Suggestion 4

def solve():
    from itertools import permutations
    s, k = input().split()
    k = int(k)
    perms = sorted(set(permutations(s)))
    print(''.join(perms[k-1]))

=======
Suggestion 5

def get_permutations(string):
    if len(string) == 1:
        return [string]
    else:
        permutations = []
        for char in string:
            for permutation in get_permutations(string.replace(char, '', 1)):
                permutations.append(char + permutation)
        return permutations

=======
Suggestion 6

def permute(s, k):
    if len(s) == 1:
        return s
    else:
        res = []
        for i, c in enumerate(s):
            for perm in permute(s[:i] + s[i+1:], k):
                res.append(c + perm)
        return sorted(res)[k-1]

s, k = input().split()
print(permute(s, int(k)))

=======
Suggestion 7

def factorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n * factorial(n - 1)

=======
Suggestion 8

def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    K -= 1
    for i in range(len(S)):
        if K == 0:
            break
        K = K // (len(S)-1-i)
    print(S[i], end='')
    S.remove(S[i])
    for i in range(len(S)):
        print(S[i], end='')

=======
Suggestion 9

def main():
    s,k=map(str,input().split())
    k=int(k)
    s=list(s)
    s.sort()
    count=0
    while count<k-1:
        i=len(s)-1
        while i>0 and s[i-1]>=s[i]:
            i-=1
        j=len(s)-1
        while s[j]<=s[i-1]:
            j-=1
        s[i-1],s[j]=s[j],s[i-1]
        s[i:]=s[len(s)-1:i-1:-1]
        count+=1
    print("".join(s))

=======
Suggestion 10

def kth_smallest_permutation(s, k):
    from math import factorial
    from collections import Counter
    from itertools import permutations
    n = len(s)
    c = Counter(s)
    d = factorial(n)
    for v in c.values():
        d //= factorial(v)
    if k > d:
        return None
    for p in permutations(sorted(s)):
        if k == 1:
            return ''.join(p)
        k -= 1
    return None
