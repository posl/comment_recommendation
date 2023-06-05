Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        while t > 0:
            k = (k + 2) // 3
            t -= 1
        print(s[k - 1])

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        t = t % 3
        if t == 0:
            print(S[k - 1])
        elif t == 1:
            print(S[k % 3 - 1])
        elif t == 2:
            print(S[(k + 1) % 3 - 1])

=======
Suggestion 3

def replace(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'a':
            s[i] = 'b'
        elif s[i] == 'b':
            s[i] = 'c'
        else:
            s[i] = 'a'
    return ''.join(s)

=======
Suggestion 4

def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_k = input().split()
        t.append(int(t_k[0]))
        k.append(int(t_k[1]))
    for i in range(q):
        for j in range(t[i]):
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
        print(s[k[i]-1])

=======
Suggestion 5

def main():
    # 读入数据
    S = input()
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    #print(S, Q, query)

    # 逆向处理
    # S_0 = S
    # S_1 = S_0.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_2 = S_1.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_3 = S_2.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_4 = S_3.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_5 = S_4.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_6 = S_5.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_7 = S_6.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_8 = S_7.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_9 = S_8.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_10 = S_9.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_11 = S_10.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_12 = S_11.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_13 = S_12.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_14 = S_13.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
    # S_15 = S_14.replace('a',

=======
Suggestion 6

def main():
    s = input()
    q = int(input())
    queries = []
    for i in range(q):
        t, k = map(int, input().split())
        queries.append((t, k))
    ans = []
    for t, k in queries:
        for i in range(t):
            s = s.replace("a", "bc").replace("b", "ca").replace("c", "ab")
        ans.append(s[k - 1])
    print(*ans, sep="\n")

=======
Suggestion 7

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k = k - 1
        if t == 1:
            k = k % len(s)
            print(s[k])
        elif t == 2:
            k = k % len(s)
            print(s[k+1])
        else:
            k = k % len(s)
            print(s[k+2])

=======
Suggestion 8

def replace(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'a':
            s[i] = 'b'
        elif s[i] == 'b':
            s[i] = 'c'
        elif s[i] == 'c':
            s[i] = 'a'
    return ''.join(s)

=======
Suggestion 9

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        k -= 1
        for i in range(t):
            s = s[k % len(s)] + s[:k % len(s)] + s[k % len(s) + 1:]
            k = k // len(s)
        print(s[0])

=======
Suggestion 10

def problem242_d():
    pass
