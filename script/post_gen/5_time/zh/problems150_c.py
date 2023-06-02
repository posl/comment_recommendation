Synthesizing 10/10 solutions

=======
Suggestion 1

def getPermutationCount(n):
    if n == 1:
        return 1
    else:
        return n*getPermutationCount(n-1)

=======
Suggestion 2

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

=======
Suggestion 3

def permutation(n, p, q):
    p_rank = 0
    q_rank = 0
    for i in range(n):
        p_rank += p[i] * 10 ** (n - i - 1)
        q_rank += q[i] * 10 ** (n - i - 1)
    return p_rank, q_rank

=======
Suggestion 4

def main():
    n = int(input())
    p = input().split()
    q = input().split()
    print(abs(p.index(q)+1-q.index(q)-1))

=======
Suggestion 5

def getNum(a):
    n = len(a)
    if n == 1:
        return 0
    else:
        b = a[1:]
        c = []
        for i in range(len(b)):
            if a[0] > b[i]:
                c.append(b[i])
        return getNum(c) + len(c)

=======
Suggestion 6

def get_min_permutation(n):
    if n == 1:
        return [1]
    else:
        return [n] + get_min_permutation(n - 1)

=======
Suggestion 7

def get_num(arr):
    num = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                num += 1
    return num

=======
Suggestion 8

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

=======
Suggestion 9

def permutationNumber(a):
    if len(a) == 1:
        return 1
    else:
        return len(a) * permutationNumber(a[1:])

=======
Suggestion 10

def find_min_permutation(n):
    return 1
