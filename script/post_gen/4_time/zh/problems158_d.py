Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t = input()
        if t == "1":
            s = s[::-1]
        else:
            f, c = t.split()[1:]
            if f == "1":
                s = c + s
            else:
                s = s + c
    print(s)

=======
Suggestion 2

def main():
    s = input()
    q = int(input())
    t = 0
    f = 0
    c = ''
    for i in range(q):
        t, f, c = input().split()
        t = int(t)
        f = int(f)
        if t == 1:
            s = s[::-1]
        else:
            if f == 1:
                s = c + s
            else:
                s = s + c
    print(s)

=======
Suggestion 3

def reverse(s):
    return s[::-1]

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            S = S[::-1]
        else:
            if query[1] == '1':
                S = query[2] + S
            else:
                S = S + query[2]
    print(S)

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            s = s[::-1]
        else:
            if query[1] == "1":
                s = query[2] + s
            else:
                s = s + query[2]
    print(s)

=======
Suggestion 6

def reverse(s):
    s = list(s)
    s.reverse()
    s = "".join(s)
    return s

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    T = []
    F = []
    C = []
    for i in range(Q):
        tmp = input().split(' ')
        T.append(tmp[0])
        if tmp[0] == '2':
            F.append(tmp[1])
            C.append(tmp[2])
    S = list(S)
    C.reverse()
    for i in range(Q):
        if T[i] == '1':
            S.reverse()
        else:
            if F[i] == '1':
                S.append(C[i])
            else:
                S.insert(0, C[i])
    print(''.join(S))
