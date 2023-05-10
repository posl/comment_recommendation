Synthesizing 10/10 solutions

=======
Suggestion 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p = list(p)
    q = list(q)
    p = [i-1 for i in p]
    q = [i-1 for i in q]
    # print(p)
    # print(q)
    # print(n)
    # print(p)
    # print(q)
    # print(p.index(0))
    # print(q.index(0))
    # print(p.index(1))
    # print(q.index(1))
    # print(p.index(2))
    # print(q.index(2))
    # print(p.index(3))
    # print(q.index(3))
    # print(p.index(4))
    # print(q.index(4))
    # print(p.index(5))
    # print(q.index(5))
    # print(p.index(6))
    # print(q.index(6))
    # print(p.index(7))
    # print(q.index(7))
    # print(p.index(8))
    # print(q.index(8))

    # print(p.index(0))
    # print(q.index(0))
    # print(p.index(1))
    # print(q.index(1))
    # print(p.index(2))
    # print(q.index(2))
    # print(p.index(3))
    # print(q.index(3))
    # print(p.index(4))
    # print(q.index(4))
    # print(p.index(5))
    # print(q.index(5))
    # print(p.index(6))
    # print(q.index(6))
    # print(p.index(7))
    # print(q.index(7))
    # print(p.index(8))
    # print(q.index(8))

    # print(p.index(0))
    # print(q.index(0))
    # print(p.index(1))
    # print(q.index(1))
    # print(p.index(2))
    # print(q.index(2))
    # print(p.index(3))
    # print(q.index(3))
    # print(p.index(4))
    # print(q.index(4))
    # print(p.index(5))
    # print(q.index(5))
    # print(p.index(6))
    # print(q.index(6))
    # print(p.index(7))

=======
Suggestion 3

def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))

    def permutation(n):
        if n == 1:
            yield (0,)
        else:
            for i in range(n):
                for j in permutation(n - 1):
                    yield j + (i,)

    def to_num(p):
        n = len(p)
        num = 0
        for i in range(n):
            num += p[i] * (n ** i)
        return num

    def solve(n, p, q):
        for i, v in enumerate(permutation(n)):
            if p == v:
                p_num = i
            if q == v:
                q_num = i
        return abs(p_num - q_num)

    print(solve(n, p, q))

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # 順列のリストを作る
    def permutation(N):
        if N == 1:
            return [[1]]
        else:
            A = permutation(N-1)
            B = []
            for a in A:
                for i in range(N):
                    b = list(a)
                    b.insert(i, N)
                    B.append(b)
            return B

    # 辞書順で何番目かを返す
    def dic_number(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1) + dic_number(N-1, A)

    # 辞書順で何番目かを返す
    def dic_number2(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1) + dic_number(N-1, A)

    # 辞書順で何番目かを返す
    def dic_number3(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1) + dic_number(N-1, A)

    # 辞書順で何番目かを返す
    def dic_number4(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1) + dic_number(N-1, A)

    # 辞書順で何番目かを返す
    def dic_number5(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    def permutation(n):
        if n == 0:
            return [[]]
        else:
            return [[x] + y for x in range(n) for y in permutation(x)]

    def index(a, l):
        return l.index(a)

    print(abs(index(p, permutation(n)) - index(q, permutation(n))))

=======
Suggestion 6

def get_permutation(n):
    if n == 1:
        return [[1]]
    else:
        return [[n] + p for p in get_permutation(n-1)] + [p + [n] for p in get_permutation(n-1)]

=======
Suggestion 7

def get_permutation_count(n):
    if n <= 1:
        return 1
    else:
        return n * get_permutation_count(n - 1)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    def permutation(n):
        if n == 1:
            return [[1]]
        else:
            return [[n] + p for p in permutation(n-1)] + [p + [n] for p in permutation(n-1)]

    def index(l, p):
        for i, v in enumerate(l):
            if v == p:
                return i

    print(abs(index(permutation(n), p) - index(permutation(n), q)))

main()

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # 順列の作成
    def permutation(N):
        if N == 1:
            return [[1]]
        else:
            return [p[:i]+[N]+p[i:] for p in permutation(N-1) for i in range(N)]

    # 順列の辞書順を求める
    def permutation_number(P):
        n = len(P)
        if n == 1:
            return 0
        else:
            return (P[-1]-1) * math.factorial(n-1) + permutation_number(P[:-1])

    # 辞書順の差を求める
    print(abs(permutation_number(P)-permutation_number(Q)))

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    p_index = 0
    q_index = 0

    for i in range(n):
        p_index += (p[i] - 1) * math.factorial(n - i - 1)
        q_index += (q[i] - 1) * math.factorial(n - i - 1)

    print(abs(p_index - q_index))
