Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    T = []
    F = []
    C = []
    for i in range(Q):
        t = input().split()
        T.append(int(t[0]))
        if len(t) == 3:
            F.append(int(t[1]))
            C.append(t[2])
    #print(T)
    #print(F)
    #print(C)
    A = list(S)
    #print(A)
    reverse = False
    for i in range(Q):
        if T[i] == 1:
            reverse = not reverse
        else:
            if reverse:
                if F[i] == 1:
                    A.append(C[i])
                else:
                    A.insert(0, C[i])
            else:
                if F[i] == 1:
                    A.insert(0, C[i])
                else:
                    A.append(C[i])
    if reverse:
        A.reverse()
    print(''.join(A))

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    is_reverse = False
    for _ in range(Q):
        query = input().split()
        if len(query) == 1:
            is_reverse = not is_reverse
        else:
            if query[1] == '1':
                if is_reverse:
                    S = S + query[2]
                else:
                    S = query[2] + S
            else:
                if is_reverse:
                    S = query[2] + S
                else:
                    S = S + query[2]
    if is_reverse:
        print(S[::-1])
    else:
        print(S)

=======
Suggestion 3

def main():
    S = input()
    Q = int(input())
    rev = False
    for _ in range(Q):
        query = list(input().split())
        if len(query) == 1:
            rev = not rev
        else:
            if query[1] == '1':
                if rev:
                    S = S + query[2]
                else:
                    S = query[2] + S
            else:
                if rev:
                    S = query[2] + S
                else:
                    S = S + query[2]
    if rev:
        S = S[::-1]
    print(S)

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    reverse = False
    for i in range(Q):
        T = list(map(str, input().split()))
        if T[0] == '1':
            reverse = not reverse
        else:
            if T[1] == '1':
                if reverse:
                    S = S + T[2]
                else:
                    S = T[2] + S
            else:
                if reverse:
                    S = T[2] + S
                else:
                    S = S + T[2]
    if reverse:
        print(S[::-1])
    else:
        print(S)

=======
Suggestion 5

def main():
    S = input()
    Q = int(input())
    rev = False
    head = []
    tail = []
    for i in range(Q):
        query = list(input().split())
        if query[0] == '1':
            rev = not rev
        else:
            if (query[1] == '1' and not rev) or (query[1] == '2' and rev):
                head.append(query[2])
            else:
                tail.append(query[2])
    head = ''.join(head)
    tail = ''.join(tail)
    if rev:
        print(tail[::-1] + S[::-1] + head[::-1])
    else:
        print(head + S + tail)

=======
Suggestion 6

def main():
    S = list(input())
    Q = int(input())
    reverse = 0
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            reverse += 1
        else:
            if (int(query[1]) + reverse) % 2 == 0:
                S.append(query[2])
            else:
                S.insert(0, query[2])
    if reverse % 2 == 1:
        S = S[::-1]
    print(''.join(S))

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    reversed = False
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            reversed = not reversed
        else:
            if query[1] == "1":
                S = query[2] + S
            else:
                S = S + query[2]
    if reversed:
        S = S[::-1]
    print(S)

=======
Suggestion 8

def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for i in range(q):
        t = list(map(str, input().split()))
        if t[0] == '1':
            rev = not rev
        else:
            if t[1] == '1':
                if rev:
                    s.append(t[2])
                else:
                    s.insert(0, t[2])
            else:
                if rev:
                    s.insert(0, t[2])
                else:
                    s.append(t[2])
    if rev:
        s = s[::-1]
    print("".join(s))

=======
Suggestion 9

def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for i in range(q):
        t, *f = input().split()
        if t == '1':
            rev = not rev
        else:
            if rev:
                if f[0] == '1':
                    s.append(f[1])
                else:
                    s.insert(0, f[1])
            else:
                if f[0] == '1':
                    s.insert(0, f[1])
                else:
                    s.append(f[1])
    if rev:
        s.reverse()
    print(''.join(s))

=======
Suggestion 10

def main():
    S = input()
    Q = int(input())

    # 0: original, 1: reversed
    rev = 0

    # 0: original, 1: reversed
    front = []
    back = []

    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            rev = 1 - rev
        else:
            if query[1] == '1':
                if rev == 0:
                    front.append(query[2])
                else:
                    back.append(query[2])
            else:
                if rev == 0:
                    back.append(query[2])
                else:
                    front.append(query[2])

    if rev == 0:
        print(''.join(front[::-1]) + S + ''.join(back))
    else:
        print(''.join(back[::-1]) + S[::-1] + ''.join(front))
