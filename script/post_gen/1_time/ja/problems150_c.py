Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    from itertools import permutations
    for i, p in enumerate(permutations(range(1, N+1)), 1):
        if list(p) == P:
            a = i
        if list(p) == Q:
            b = i

    print(abs(a-b))

=======
Suggestion 2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    A = []
    B = []
    for i in range(N):
        A.append(i+1)
        B.append(i+1)
    a = 0
    b = 0
    for i in range(N):
        a += (A.index(P[i])) * (math.factorial(N-i-1))
        A.remove(P[i])
        b += (B.index(Q[i])) * (math.factorial(N-i-1))
        B.remove(Q[i])
    print(abs(a-b))

=======
Suggestion 4

def main():
    n = int(input())
    p = input().split()
    q = input().split()
    p = [int(i) for i in p]
    q = [int(i) for i in q]
    p = list(map(lambda x: x - 1, p))
    q = list(map(lambda x: x - 1, q))
    # print(p)
    # print(q)
    # print(p.index(2))
    # print(q.index(2))
    import math
    from itertools import permutations
    # print(math.factorial(n))
    # print(list(permutations(range(1, n+1))))
    # print(list(permutations(range(1, n+1))).index(tuple(p)))
    # print(list(permutations(range(1, n+1))).index(tuple(q)))
    print(abs(list(permutations(range(1, n+1))).index(tuple(p)) - list(permutations(range(1, n+1))).index(tuple(q))))

=======
Suggestion 5

def getPermutation(n):
    if n == 1:
        return [[1]]
    else:
        return [[n] + p for p in getPermutation(n-1)] + [p + [n] for p in getPermutation(n-1)]

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    #print(N)
    #print(P)
    #print(Q)
    def permutation(N, P):
        if N == 1:
            return [P]
        ret = []
        for i in range(N):
            for p in permutation(N-1, P[:i] + P[i+1:]):
                ret.append([P[i]] + p)
        return ret
    def calc(N, P, Q):
        P_permutation = permutation(N, P)
        Q_permutation = permutation(N, Q)
        P_permutation.sort()
        Q_permutation.sort()
        P_permutation_index = 0
        Q_permutation_index = 0
        for i in range(len(P_permutation)):
            if P_permutation[i] == P:
                P_permutation_index = i
            if Q_permutation[i] == Q:
                Q_permutation_index = i
        print(abs(P_permutation_index - Q_permutation_index))
    calc(N, P, Q)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    # print(N)
    # print(P)
    # print(Q)
    def permutation(n):
        if n == 0:
            return [[]]
        else:
            return [[i] + p for i in range(n) for p in permutation(n - 1) if i not in p]

    p_list = permutation(N)
    # print(p_list)
    p_num = 0
    q_num = 0
    for i in range(len(p_list)):
        if p_list[i] == P:
            p_num = i + 1
        if p_list[i] == Q:
            q_num = i + 1
    # print(p_num)
    # print(q_num)
    print(abs(p_num - q_num))

=======
Suggestion 8

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]

    def calc_num(l):
        n = 0
        for i in range(len(l)):
            n += l[i] * (math.factorial(len(l) - i - 1))
        return n

    print(abs(calc_num(P) - calc_num(Q)))

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    def count_permutation(N, P):
        count = 0
        for i in range(1, N):
            count += i * math.factorial(N - i)
            for j in range(i + 1, N):
                if P[i - 1] < P[j - 1]:
                    count -= math.factorial(N - i - 1)
        return count

    print(abs(count_permutation(N, P) - count_permutation(N, Q)))

=======
Suggestion 10

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # 1,2,...,N の順列を作成
    # 1,2,...,N の順列を作成
    def perm(N):
        if N == 1:
            return [[1]]
        else:
            return [[N] + p for p in perm(N-1)] + [p + [N] for p in perm(N-1)]
    # 1,2,...,N の順列を作成
    # 1,2,...,N の順列を作成
    def perm(N):
        if N == 1:
            return [[1]]
        else:
            return [[N] + p for p in perm(N-1)] + [p + [N] for p in perm(N-1)]

    Pp = perm(N)
    #print(Pp)
    #print(P)
    #print(Q)
    #print(Pp.index(P))
    #print(Pp.index(Q))
    print(abs(Pp.index(P) - Pp.index(Q)))
