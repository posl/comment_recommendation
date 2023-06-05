Synthesizing 10/10 solutions

=======
Suggestion 1

def permutation(n):
    if n == 1:
        return [[1]]
    else:
        return [[n] + p for p in permutation(n-1)] + [p + [n] for p in permutation(n-1)]

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    def permutation_to_int(p):
        ret = 0
        for i in range(len(p)):
            ret += p[i] * 10 ** (len(p) - i - 1)
        return ret

    p_int = permutation_to_int(p)
    q_int = permutation_to_int(q)
    print(abs(p_int - q_int))

=======
Suggestion 3

def main():
    # N = int(input())
    # P = list(map(int, input().split()))
    # Q = list(map(int, input().split()))
    N = 3
    P = [1, 3, 2]
    Q = [3, 1, 2]
    print(abs(index(P) - index(Q)))

=======
Suggestion 4

def solve():
    n = int(input())
    p = [int(i) for i in input().split()]
    q = [int(i) for i in input().split()]

    def permutation_index(p):
        index = 0
        for i in range(len(p)):
            index += p[i] - 1
            index *= len(p) - i - 1
        return index

    print(abs(permutation_index(p) - permutation_index(q)))


solve()

=======
Suggestion 5

def permutate(n):
    if n == 0:
        return [[]]
    else:
        return [[x] + p for x in range(n) for p in permutate(n - 1) if x not in p]

=======
Suggestion 6

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    q = [int(x) for x in input().split()]

    def permutation_to_number(l):
        if len(l) == 1:
            return 0
        return l[-1] + permutation_to_number([x-1 for x in l[:-1] if x > l[-1]])

    print(abs(permutation_to_number(p) - permutation_to_number(q)))

=======
Suggestion 7

def solve(n,p,q):
    l = []
    for i in range(n):
        l.append(i+1)
    p_index = 0
    q_index = 0
    for i in range(n):
        p_index += (l.index(p[i])) * (n-i-1)
        l.remove(p[i])
        q_index += (l.index(q[i])) * (n-i-1)
        l.remove(q[i])
    return abs(p_index - q_index)

=======
Suggestion 8

def solve(n, p, q):
    def permutation(n):
        if n == 0:
            return [[]]
        else:
            return [[i] + perm for i in range(1, n + 1) for perm in permutation(n - 1) if i not in perm]

    def index(p):
        return permutation(len(p)).index(p) + 1

    return abs(index(p) - index(q))

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    print(abs(p.index(1) - q.index(1)))

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split(" ")))
    q = list(map(int, input().split(" ")))
    print(abs(p.index(1) - q.index(1)))
