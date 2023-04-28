Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    a = 0
    b = 0
    for i in range(n):
        a += p[i] * (n-i-1)
        b += q[i] * (n-i-1)

    print(abs(a-b))

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_index = 0
    q_index = 0
    for i in range(n):
        p_index += p[i] * (n - i - 1) * factorial(n - i - 1)
        q_index += q[i] * (n - i - 1) * factorial(n - i - 1)
    print(abs(p_index - q_index))

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    #print(N)
    #print(P)
    #print(Q)
    #print(len(P))
    #print(len(Q))
    #print(P[0])
    #print(Q[0])

    #順列を作成
    #Pの順列を作成
    P_array = []
    for i in range(N):
        P_array.append(i+1)
    #print(P_array)

    #Qの順列を作成
    Q_array = []
    for i in range(N):
        Q_array.append(i+1)
    #print(Q_array)

    #P,Qの順列を作成
    import itertools
    P_permutations = list(itertools.permutations(P_array))
    #print(P_permutations)
    Q_permutations = list(itertools.permutations(Q_array))
    #print(Q_permutations)

    #P,Qの順列を辞書順にソート
    P_permutations.sort()
    #print(P_permutations)
    Q_permutations.sort()
    #print(Q_permutations)

    #P,Qの順列が何番目にあるかを取得
    P_count = 0
    Q_count = 0
    for i in range(len(P_permutations)):
        if P_permutations[i] == tuple(P):
            P_count = i + 1
    #print(P_count)
    for i in range(len(Q_permutations)):
        if Q_permutations[i] == tuple(Q):
            Q_count = i + 1
    #print(Q_count)

    #|a - b|を出力
    print(abs(P_count - Q_count))

=======
Suggestion 4

def permutation(n):
    if n == 1:
        return [[1]]
    else:
        result = []
        for p in permutation(n-1):
            for i in range(n):
                result.append(p[:i] + [n] + p[i:])
        return result

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

p_list = permutation(n)
p_list.sort()
p_index = p_list.index(p)
q_index = p_list.index(q)
print(abs(p_index - q_index))

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # 順列生成
    def permutations_count(n, r):
        return math.factorial(n) // math.factorial(n - r)

    def permutations_with_replacement_count(n, r):
        return (n + r - 1) * math.factorial(n - 1) // math.factorial(n - r)

    # 順列生成
    def permutations(iterable, r=None):
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n - r, -1))
        yield tuple(pool[i] for i in indices[:r])
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                return

    # 順列生成
    def permutations_with_replacement(iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        for indices in product(range(n), repeat=r):
            if sorted(indices) == list(indices):
                yield tuple(pool[i] for i in indices)

    import math
    from itertools import product

    P_permutations = list(permutations(range(1,N+1)))
    Q_permutations = list(permutations(range(1,N+1)))

    for i in range(len(P_permutations)):
        if P_permutations[i] == tuple(P):
            a = i+1
        if Q_permutations[i] == tuple(Q):
            b = i+1

    print(abs(a-b))

main()

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    # 順列の辞書順での番号を求める
    def get_num(l):
        num = 0
        for i in range(n):
            num += l[i] * (n-i) * (n-i-1) // 2
        return num

    print(abs(get_num(p) - get_num(q)))

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    def dfs(a, l):
        if len(a) == n:
            return int("".join(map(str, a)))
        for i in range(1, n+1):
            if i in a:
                continue
            a.append(i)
            l.append(dfs(a, l))
            a.pop()
        return l

    l = dfs([], [])
    print(abs(l.index(int("".join(map(str, p)))) - l.index(int("".join(map(str, q))))))

=======
Suggestion 8

def calc(n, p, q):
    a = 0
    b = 0
    for i in range(n):
        a = a + (p[i] - 1) * factorial(n - i - 1, p)
        b = b + (q[i] - 1) * factorial(n - i - 1, q)
        #print(a, b, p[i], q[i])
    return abs(a - b)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    #順列の数を計算
    P_num = 0
    Q_num = 0
    for i in range(N):
        P_num += P[i] * (N - 1 - i) * math.factorial(N - 1 - i)
        Q_num += Q[i] * (N - 1 - i) * math.factorial(N - 1 - i)
    print(abs(P_num - Q_num))

=======
Suggestion 10

def get_permutation(n):
    result = []
    def _get_permutation(n, tmp):
        if len(tmp) == n:
            result.append(tmp)
            return
        for i in range(1, n+1):
            if i in tmp:
                continue
            _get_permutation(n, tmp + [i])
    _get_permutation(n, [])
    return result

import itertools
