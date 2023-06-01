Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    t_k = [list(map(int, input().split())) for _ in range(Q)]

    for t, k in t_k:
        t = t % 3
        for _ in range(t):
            S = S.replace('a', 'bc')
            S = S.replace('b', 'ca')
            S = S.replace('c', 'ab')
        print(S[k-1])

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        if t == 1:
            t = 2
        elif t == 2:
            t = 1
        if k >= len(S):
            k %= len(S)
        print(S[k])

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    t_k = []
    for i in range(q):
        t_k.append(list(map(int, input().split())))
    # print(t_k)
    for i in range(q):
        s = S(s, t_k[i][0])
        print(s[t_k[i][1]-1])

=======
Suggestion 4

def solve():
    s = input()
    q = int(input())
    tks = []
    for _ in range(q):
        tk = input().split()
        tk[0] = int(tk[0])
        tk[1] = int(tk[1])
        tks.append(tk)
    for tk in tks:
        t = tk[0]
        k = tk[1]
        for i in range(t):
            s = s.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
        print(s[k - 1])

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    t_k = []
    for i in range(q):
        t_k.append(list(map(int, input().split())))
    #print(t_k)
    for i in range(q):
        t = t_k[i][0]
        k = t_k[i][1]
        for j in range(t):
            s = s.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
        print(s[k-1])

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    #print(S, Q, queries)
    #S = 'ABC'
    #Q = 4
    #queries = [[0, 1], [1, 1], [1, 3], [1, 6]]

    #S = 'CBBAACCCCC'
    #Q = 5
    #queries = [[57530144230160008, 659279164847814847], [29622990657296329, 861239705300265164], [509705228051901259, 994708708957785197], [176678501072691541, 655134104344481648], [827291290937314275, 407121144297426665]]

    #S = 'ABC'
    #Q = 1
    #queries = [[0, 1]]

    #S = 'ABC'
    #Q = 1
    #queries = [[1, 1]]

    #S = 'ABC'
    #Q = 1
    #queries = [[1, 3]]

    #S = 'ABC'
    #Q = 1
    #queries = [[1, 6]]

    #S = 'ABC'
    #Q = 1
    #queries = [[1, 7]]

    #S = 'ABC'
    #Q = 1
    #queries = [[1, 8]]

    #S = 'ABC'
    #Q = 1
    #queries = [[2, 1]]

    #S = 'ABC'
    #Q = 1
    #queries = [[2, 3]]

    #S = 'ABC'
    #Q = 1
    #queries = [[2, 6]]

    #S = 'ABC'
    #Q = 1
    #queries = [[2, 7]]

    #S = 'ABC'
    #Q = 1
    #queries = [[2, 8]]

    #S = 'ABC'
    #Q = 1
    #queries = [[3, 1]]

    #S = 'ABC'
    #Q = 1
    #queries = [[3, 3]]

=======
Suggestion 7

def main():
    s = input()
    q = int(input())
    t_k = []
    for i in range(q):
        t_k.append(list(map(int,input().split())))
    # print(s)
    # print(q)
    # print(t_k)
    for i in range(q):
        t = t_k[i][0]
        k = t_k[i][1]
        # print(t)
        # print(k)
        # print(s)
        for j in range(t):
            s = s.replace('a','bc')
            s = s.replace('b','ca')
            s = s.replace('c','ab')
        print(s[k-1])

=======
Suggestion 8

def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
    for i in range(q):
        t_i = t[i]
        k_i = k[i]
        for j in range(t_i):
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
        print(s[k_i-1])

=======
Suggestion 9

def main():
    S = input()
    Q = int(input())
    t_k = [list(map(int, input().split())) for _ in range(Q)]

    t_max = max(t_k, key=lambda x: x[0])[0]
    s = S
    for i in range(t_max):
        s = s.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    for t, k in t_k:
        print(s[t:][k-1])

=======
Suggestion 10

def tr(s):
    return s.replace('a','bc').replace('b','ca').replace('c','ab')

S = input()
Q = int(input())
T = []
K = []
for i in range(Q):
    a,b = map(int,input().split())
    T.append(a)
    K.append(b)

for i in range(Q):
    s = S
    t = T[i]
    k = K[i]
    for j in range(t):
        s = tr(s)
    print(s[k-1])
