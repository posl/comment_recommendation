Synthesizing 10/10 solutions

=======
Suggestion 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

=======
Suggestion 2

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]
    a = P.index(1)
    b = Q.index(1)
    for i in range(N):
        if P[i] > P[a]:
            a += 1
        if Q[i] > Q[b]:
            b += 1
    print(abs(a - b))

=======
Suggestion 3

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]

    P = [x - 1 for x in P]
    Q = [x - 1 for x in Q]

    #print(P)
    #print(Q)

    P = tuple(P)
    Q = tuple(Q)

    #print(P)
    #print(Q)

    #print(type(P))
    #print(type(Q))

    X = list(range(N))
    X = tuple(X)

    #print(X)

    #print(type(X))

    import itertools

    a = 0
    b = 0

    for i, x in enumerate(itertools.permutations(X)):
        if x == P:
            a = i
        if x == Q:
            b = i

    print(abs(a - b))

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    #N = 3
    #P = [1, 3, 2]
    #Q = [3, 1, 2]
    #N = 8
    #P = [7, 3, 5, 4, 2, 1, 6, 8]
    #Q = [3, 8, 2, 5, 4, 6, 7, 1]
    #N = 3
    #P = [1, 2, 3]
    #Q = [1, 2, 3]
    #N = 3
    #P = [3, 2, 1]
    #Q = [1, 2, 3]
    #N = 4
    #P = [4, 3, 2, 1]
    #Q = [1, 2, 3, 4]
    #N = 4
    #P = [1, 2, 3, 4]
    #Q = [4, 3, 2, 1]
    #N = 5
    #P = [1, 2, 3, 4, 5]
    #Q = [5, 4, 3, 2, 1]
    #N = 5
    #P = [5, 4, 3, 2, 1]
    #Q = [1, 2, 3, 4, 5]
    #N = 6
    #P = [1, 2, 3, 4, 5, 6]
    #Q = [6, 5, 4, 3, 2, 1]
    #N = 6
    #P = [6, 5, 4, 3, 2, 1]
    #Q = [1, 2, 3, 4, 5, 6]
    #N = 7
    #P = [1, 2, 3, 4, 5, 6, 7]
    #Q = [7

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int,input().split()))
    Q = list(map(int,input().split()))
    from itertools import permutations
    perm = list(permutations(range(1,N+1)))
    print(abs(perm.index(tuple(P))-perm.index(tuple(Q))))

=======
Suggestion 6

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # create a list of numbers from 1 to N
    numbers = list(range(1, N + 1))
    # create a list of all permutations of the list of numbers
    perms = list(itertools.permutations(numbers))
    # get the index of the permutation P in the list of all permutations
    i1 = perms.index(tuple(P))
    # get the index of the permutation Q in the list of all permutations
    i2 = perms.index(tuple(Q))
    # print the difference of the indices
    print(abs(i1 - i2))

=======
Suggestion 8

def get_smaller_count ( perm ) :
    smaller_count = 0
    for i in range ( len ( perm ) ) :
        for j in range ( i + 1 , len ( perm ) ) :
            if perm [ i ] > perm [ j ] :
                smaller_count += 1
    return smaller_count

=======
Suggestion 9

def permutation(n):
    def perm(n, i, j):
        if i == j:
            yield n
        else:
            for k in range(i, j):
                n[i], n[k] = n[k], n[i]
                for x in perm(n, i + 1, j):
                    yield x
                n[i], n[k] = n[k], n[i]
    return perm(n, 0, len(n))

=======
Suggestion 10

def get_permutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    # n! / (n-k)!
    # n! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8
    # (n-k)! = 1 * 2 * 3 * 4 * 5 * 6 * 7
    # n! = 40320
    # (n-k)! = 5040
    # n! / (n-k)! = 8
    # n! = 40320
    # (n-k)! = 40320
    # n! / (n-k)! = 1
    # n! = 40320
    # (n-k)! = 362880
    # n! / (n-k)! = 1/9
    # n! = 40320
    # (n-k)! = 3628800
    # n! / (n-k)! = 1/90
    # n! = 40320
    # (n-k)! = 36288000
    # n! / (n-k)! = 1/720
    # n! = 40320
    # (n-k)! = 362880000
    # n! / (n-k)! = 1/7200
    # n! = 40320
    # (n-k)! = 3628800000
    # n! / (n-k)! = 1/50400
    # n! = 40320
    # (n-k)! = 36288000000
    # n! / (n-k)! = 1/504000
    # n! = 40320
    # (n-k)! = 362880000000
    # n! / (n-k)! = 1/4032000
    # n! = 40320
    # (n-k)! = 3628800000000
    # n! / (n-k)! = 1/40320000
    # n! = 40320
    # (n-k)! = 36288000000000
    # n! / (n-k)! = 1/362880
