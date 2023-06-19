Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k -= 1
        for i in range(t):
            k = (k + 1) % len(s)
            if s[k] == "a":
                s = s[:k] + "bc" + s[k + 1:]
            elif s[k] == "b":
                s = s[:k] + "ca" + s[k + 1:]
            elif s[k] == "c":
                s = s[:k] + "ab" + s[k + 1:]
        print(s[k])

=======
Suggestion 2

def solve():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        print(s[k] if t == 0 else s[(k + t) % len(s)])

=======
Suggestion 3

def main():
    S = input()
    Q = int(input())
    t = []
    k = []
    for i in range(Q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
    #print(S)
    #print(Q)
    #print(t)
    #print(k)
    for i in range(Q):
        S_i = S
        for j in range(t[i]):
            S_i = S_i.replace('a', 'bc')
            S_i = S_i.replace('b', 'ca')
            S_i = S_i.replace('c', 'ab')
        print(S_i[k[i]-1])

=======
Suggestion 4

def main():
    S=input()
    Q=int(input())
    for i in range(Q):
        t,k=map(int,input().split())
        t=t%(3*10**18)
        for j in range(t):
            S=S.replace('a','bc')
            S=S.replace('b','ca')
            S=S.replace('c','ab')
        print(S[k-1])

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    t_k = []
    for i in range(q):
        t_k.append(list(map(int, input().split())))
    for i in range(q):
        t = t_k[i][0]
        k = t_k[i][1]
        if t == 0:
            print(s[k - 1])
        else:
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
            print(s[k - 1])

=======
Suggestion 6

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
            print(s[(k+1)%len(s)])
        else:
            print(s[(k+2)%len(s)])

=======
Suggestion 7

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
Suggestion 8

def main():
    s = input()
    q = int(input())

    # 0 1 2 3 4 5 6 7 8 9
    # 0 1 2 3 4 5 6 7 8 9
    # 0 1 2 3 4 0 1 2 3 4
    # 0 1 2 3 0 1 2 3 0 1
    # 0 1 2 0 1 2 0 1 2 0
    # 0 1 0 1 0 1 0 1 0 1
    # 0 0 1 0 0 1 0 0 1 0
    # 0 1 2 3 4 5 6 7 8 9
    # 0 1 2 3 4 5 6 7 8 9
    # 0 1 2 3 4 0 1 2 3 4
    # 0 1 2 3 0 1 2 3 0 1
    # 0 1 2 0 1 2 0 1 2 0
    # 0 1 0 1 0 1 0 1 0 1
    # 0 0 1 0 0 1 0 0 1 0
    # 0 1 2 3 4 5 6 7 8 9
    # 0 1 2 3 4 5 6 7 8 9
    # 0 1 2 3 4 0 1 2 3 4
    # 0 1 2 3 0 1 2 3 0 1
    # 0 1 2 0 1 2 0 1 2 0
    # 0 1 0 1 0 1 0 1 0 1
    # 0 0 1 0 0 1 0 0 1 0
    # 0

=======
Suggestion 9

def main():
    s = input()
    q = int(input())
    tks = []
    for i in range(q):
        tks.append(tuple(map(int, input().split())))

    for t, k in tks:
        t = t % 3
        if t == 0:
            print(s[k-1])
        elif t == 1:
            print(s[k-1].translate(str.maketrans('abc', 'bca')))
        else:
            print(s[k-1].translate(str.maketrans('abc', 'cab')))

=======
Suggestion 10

def main():
    s = input()
    q = int(input())
    t = []
    k = []
    for i in range(q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)

    # print(s, q, t, k)

    # print(len(s))
    # print(len(t))
    # print(len(k))

    # print(s[0:3])

    # print(s[0])

    # print(s[1])
    # print(s[2])

    # print(s[3])

    # print(s[4])
    # print(s[5])

    # print(s[6])

    # print(s[7])
    # print(s[8])

    # print(s[9])

    # print(s[10])
    # print(s[11])

    # print(s[12])

    # print(s[13])
    # print(s[14])

    # print(s[15])

    # print(s[16])
    # print(s[17])

    # print(s[18])

    # print(s[19])
    # print(s[20])

    # print(s[21])

    # print(s[22])
    # print(s[23])

    # print(s[24])

    # print(s[25])
    # print(s[26])

    # print(s[27])

    # print(s[28])
    # print(s[29])

    # print(s[30])

    # print(s[31])
    # print(s[32])

    # print(s[33])

    # print(s[34])
    # print(s[35])

    # print(s[36])

    # print(s[37])
    # print(s[38])

    # print(s[39])

    # print(s[40])
    # print(s[41])

    # print(s[42])

    # print(s[43])
    # print(s[44])

    # print(s[45])

    # print(s[46])
    # print(s[47])

    # print(s[48])

    # print(s[49])
    # print(s[50])

    # print(s[51])

    # print(s[52])
    # print(s[53])

    # print(s[54])

    # print(s[55])
    # print(s[56])

    # print(s[57])

    #
