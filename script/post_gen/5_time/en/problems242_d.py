Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    T = []
    K = []
    for i in range(Q):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
    for i in range(Q):
        s = S
        t = T[i]
        k = K[i]
        for j in range(t):
            s = s.replace('A','BC')
            s = s.replace('B','CA')
            s = s.replace('C','AB')
        print(s[k-1])

=======
Suggestion 2

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
        s_i = s
        t_i = t[i]
        k_i = k[i]

        #print("s_i: " + s_i)
        #print("t_i: " + str(t_i))
        #print("k_i: " + str(k_i))

        for j in range(t_i):
            s_i = s_i.replace("A", "BC")
            s_i = s_i.replace("B", "CA")
            s_i = s_i.replace("C", "AB")

        #print("s_i: " + s_i)

        print(s_i[k_i-1])

=======
Suggestion 3

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
        s = s * 2
        t_i = t[i]
        k_i = k[i]
        if t_i > 0:
            s = s[t_i:]
        l = len(s)
        if k_i < l:
            print(s[k_i])
        else:
            print(s[k_i % l])

=======
Suggestion 4

def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)

    #print(s)
    #print(q)
    #print(t)
    #print(k)

    #print(s[0])

    for i in range(q):
        s_i = s
        t_i = t[i]
        k_i = k[i]
        for j in range(t_i):
            s_i = s_i.replace("A","BC")
            s_i = s_i.replace("B","CA")
            s_i = s_i.replace("C","AB")
        print(s_i[k_i-1])

=======
Suggestion 5

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        for j in range(t):
            if S[k] == 'A':
                S = S[:k] + 'BC' + S[k+1:]
            elif S[k] == 'B':
                S = S[:k] + 'CA' + S[k+1:]
            elif S[k] == 'C':
                S = S[:k] + 'AB' + S[k+1:]
            k = (k + 2) % len(S)
        print(S[k])

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    query = []
    for i in range(Q):
        t, k = map(int, input().split())
        query.append([t, k])
    t_max = max([t for t, k in query])

    s = S
    for t in range(1, t_max+1):
        s = s.replace('A', 'BC')
        s = s.replace('B', 'CA')
        s = s.replace('C', 'AB')
    for t, k in query:
        print(s[k-1])

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    t_k = [list(map(int, input().split())) for _ in range(Q)]

    t_max = max([t for t, k in t_k])

    # Sの文字数を2倍、3倍、4倍と増やしていく
    for i in range(1, t_max + 1):
        S += S
        S += S
        S += S

    # Sの文字数を2倍、3倍、4倍と増やしていく
    for i in range(1, t_max + 1):
        S += S
        S += S
        S += S

    # Sの文字数を2倍、3倍、4倍と増やしていく
    for i in range(1, t_max + 1):
        S += S
        S += S
        S += S

    # Sの文字数を2倍、3倍、4倍と増やしていく
    for i in range(1, t_max + 1):
        S += S
        S += S
        S += S

    # Sの文字数を2倍、3倍、4倍と増やしていく
    for i in range(1, t_max + 1):
        S += S
        S += S
        S += S

    # Sの文字数を2倍、3倍、4倍と増やしていく
    for i in range(1, t_max + 1):
        S += S
        S += S
        S += S

    # Sの文字数を2倍、3倍、4倍と増やしていく
    for i in range(1, t_max + 1):
        S += S
        S += S
        S += S

    # Sの文字数を2倍、3倍、4倍と増やしていく
    for i in range(1, t_max + 1):
        S += S
        S += S
        S += S

    # Sの文字数を2倍、3倍、4倍と増やしていく
    for i in

=======
Suggestion 8

def main():
    S = input()
    Q = int(input())
    s = S
    t = 0
    for i in range(Q):
        t_i, k_i = map(int, input().split())
        t_i -= t
        t = t_i
        k_i -= 1
        s = s[k_i:] + s[:k_i]
        s = s.replace("A", "BC")
        s = s.replace("B", "CA")
        s = s.replace("C", "AB")
        print(s[0])

=======
Suggestion 9

def solve():
    s = input()
    q = int(input())
    n = len(s)

    # 0: A
    # 1: B
    # 2: C
    d = {'A': 0, 'B': 1, 'C': 2}

    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    e = {'A': 1, 'B': 2, 'C': 0}

    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    f = {'A': 2, 'B': 0, 'C': 1}

    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    g = {'A': 1, 'B': 0, 'C': 2}

    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    h = {'A': 2, 'B': 1, 'C': 0}

    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    i = {'A': 0, 'B': 2, 'C': 1}

    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    j = {'A': 0, 'B': 1, 'C': 2}

    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    k = {'A': 2, 'B': 0, 'C': 1}

    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    l = {'A': 1, 'B': 2, 'C': 0}

    # 0: A -> BC
    # 1: B -> CA
    # 2: C -> AB
    m = {'A': 0, 'B': 2, 'C': 1}

    # 0: A ->

=======
Suggestion 10

def AtoBC(s):
    return s.replace('A','BC')
