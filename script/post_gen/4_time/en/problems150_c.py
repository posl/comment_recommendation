Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    P = [i - 1 for i in P]
    Q = [i - 1 for i in Q]
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i
    perm = [i for i in range(N)]
    perm = list(itertools.permutations(perm))
    perm.sort()
    perm = [list(i) for i in perm]
    a = perm.index(P)
    b = perm.index(Q)
    print(abs(a - b))

=======
Suggestion 2

def next_permutation(p):
    i = len(p) - 1
    while i > 0 and p[i-1] >= p[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(p) - 1
    while p[j] <= p[i-1]:
        j -= 1
    p[i-1], p[j] = p[j], p[i-1]
    j = len(p) - 1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1
    return True

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    from itertools import permutations
    perms = list(permutations(range(1, N+1)))
    print(abs(perms.index(tuple(P)) - perms.index(tuple(Q))))

=======
Suggestion 4

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

=======
Suggestion 5

def permutations(n):
    if n == 1:
        return [[1]]
    else:
        return [[i] + p for i in range(1, n + 1) for p in permutations(n - 1) if i not in p]

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    from itertools import permutations
    P = list(permutations(P))
    Q = list(permutations(Q))
    P.sort()
    Q.sort()
    print(abs(P.index(tuple(P)) - Q.index(tuple(Q))))

=======
Suggestion 7

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

=======
Suggestion 8

def get_permutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    k = k - 1
    nums = [i for i in range(1, n + 1)]
    res = ''
    while n > 0:
        n -= 1
        index, k = divmod(k, math.factorial(n))
        res += str(nums[index])
        nums.remove(nums[index])
    return res

=======
Suggestion 9

def calc(n, p, q):
    from itertools import permutations
    perm = list(permutations(range(1, n + 1)))
    return abs(perm.index(tuple(p)) - perm.index(tuple(q)))
