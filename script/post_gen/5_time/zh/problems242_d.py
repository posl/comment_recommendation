Synthesizing 10/10 solutions

=======
Suggestion 1

def replace(s):
    s = s.replace("a","bc")
    s = s.replace("b","ca")
    s = s.replace("c","ab")
    return s

=======
Suggestion 2

def main():
    #读入字符串
    s = input()
    #读入查询数
    q = int(input())
    #读入查询
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    #处理查询
    for t, k in query:
        #计算字符串的长度
        l = len(s)
        #计算循环次数
        n = t % 3
        #循环替换
        for i in range(n):
            s = s.replace("a", "bc")
            s = s.replace("b", "ca")
            s = s.replace("c", "ab")
        #打印结果
        print(s[k-1])

=======
Suggestion 3

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        if t == 0:
            print(S[k])
        elif t == 1:
            print(S[k % 3 + 1] if S[k] == 'a' else S[k % 3 - 1])
        else:
            print(S[k % 3 - 1] if S[k] == 'c' else S[k % 3 + 1])

=======
Suggestion 4

def conv(s):
    return s.replace('a','bc').replace('b','ca').replace('c','ab')

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_i,k_i = map(int,input().split())
        t.append(t_i)
        k.append(k_i)
    for i in range(q):
        s_i = s
        for j in range(t[i]):
            s_i = s_i.replace('a','bc')
            s_i = s_i.replace('b','ca')
            s_i = s_i.replace('c','ab')
        print(s_i[k[i]-1])

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    t_k_list = [None] * Q
    for i in range(Q):
        t_k_list[i] = [int(x) for x in input().split()]

    # print(S)
    # print(Q)
    # print(t_k_list)

    for i in range(Q):
        t = t_k_list[i][0]
        k = t_k_list[i][1]
        for j in range(t):
            S = S.replace('a', 'bc')
            S = S.replace('b', 'ca')
            S = S.replace('c', 'ab')
        print(S[k - 1])

=======
Suggestion 7

def get_next(S):
    next = [0] * len(S)
    next[0] = -1
    i = 0
    j = -1
    while i < len(S) - 1:
        if j == -1 or S[i] == S[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next

=======
Suggestion 8

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k = k - 1
        for j in range(t):
            k = (k + 1) % len(s)
            if s[k] == "a":
                s = s[:k] + "bc" + s[k+1:]
            elif s[k] == "b":
                s = s[:k] + "ca" + s[k+1:]
            else:
                s = s[:k] + "ab" + s[k+1:]
        print(s[k])

=======
Suggestion 9

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k -= 1
        if t == 1:
            s = s[k:] + s[:k]
        elif t == 2:
            s = s[k:] + s[:k]
            s = s.replace('A', 'b').replace('B', 'c').replace('C', 'a')
        print(s[0])

=======
Suggestion 10

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k = k - 1
        if t == 0:
            print(s[k])
        elif t == 1:
            if s[k] == 'a':
                print('b')
            elif s[k] == 'b':
                print('c')
            elif s[k] == 'c':
                print('a')
        elif t == 2:
            if s[k] == 'a':
                print('c')
            elif s[k] == 'b':
                print('a')
            elif s[k] == 'c':
                print('b')
