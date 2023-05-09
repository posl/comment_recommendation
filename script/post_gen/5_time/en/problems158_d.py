Synthesizing 10/10 solutions

=======
Suggestion 1

def reverse(s):
    return s[::-1]

s = input()
q = int(input())

for i in range(q):
    t = input().split()
    if t[0] == '1':
        s = reverse(s)
    else:
        if t[1] == '1':
            s = t[2] + s
        else:
            s = s + t[2]

print(s)

=======
Suggestion 2

def main():
    s = input()
    q = int(input())
    t = []
    f = []
    c = []
    for i in range(q):
        temp = input().split()
        t.append(int(temp[0]))
        if t[i] == 2:
            f.append(int(temp[1]))
            c.append(temp[2])
    r = 0
    for i in range(q):
        if t[i] == 1:
            r += 1
    r = r % 2
    for i in range(q):
        if t[i] == 2:
            if f[i] == 1:
                if r == 0:
                    s = c[i] + s
                else:
                    s = s + c[i]
            else:
                if r == 0:
                    s = s + c[i]
                else:
                    s = c[i] + s
        else:
            r = 1 - r
    if r == 1:
        s = s[::-1]
    print(s)

=======
Suggestion 3

def main():
    s = input()
    s = list(s)
    q = int(input())
    reverse = False
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            reverse = not reverse
        else:
            f = int(t[1])
            c = t[2]
            if f == 1:
                if reverse:
                    s.append(c)
                else:
                    s.insert(0, c)
            else:
                if reverse:
                    s.insert(0, c)
                else:
                    s.append(c)
    if reverse:
        s.reverse()
    print(''.join(s))

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    T = [0]*Q
    F = [0]*Q
    C = ['']*Q
    for i in range(Q):
        T[i] = input()
        if T[i] == '1':
            continue
        else:
            F[i], C[i] = input().split()
            F[i] = int(F[i])

    S = list(S)
    reverse = 0
    for i in range(Q):
        if T[i] == '1':
            reverse = 1 - reverse
        else:
            if F[i] == 1:
                if reverse == 0:
                    S.insert(0, C[i])
                else:
                    S.append(C[i])
            else:
                if reverse == 0:
                    S.append(C[i])
                else:
                    S.insert(0, C[i])

    if reverse == 0:
        print(''.join(S))
    else:
        S = S[::-1]
        print(''.join(S))

=======
Suggestion 5

def reverse(s):
    return s[::-1]

s = input()
q = int(input())

for i in range(q):
    query = input().split()
    if query[0] == "1":
        s = reverse(s)
    elif query[1] == "1":
        s = query[2] + s
    else:
        s = s + query[2]

print(s)

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    S = list(S)
    reverse = 0
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            reverse += 1
        else:
            if query[1] == "1":
                if reverse % 2 == 0:
                    S.insert(0, query[2])
                else:
                    S.append(query[2])
            else:
                if reverse % 2 == 0:
                    S.append(query[2])
                else:
                    S.insert(0, query[2])
    if reverse % 2 == 1:
        S.reverse()
    print("".join(S))

=======
Suggestion 7

def main():
    s = input()
    q = int(input())
    reverse = False
    head = []
    tail = []
    for _ in range(q):
        cmd = input().split()
        if cmd[0] == '1':
            reverse = not reverse
        else:
            if cmd[1] == '1':
                if reverse:
                    tail.append(cmd[2])
                else:
                    head.append(cmd[2])
            else:
                if reverse:
                    head.append(cmd[2])
                else:
                    tail.append(cmd[2])
    if reverse:
        s = s[::-1]
        head, tail = tail, head
    print(''.join(head) + s + ''.join(tail))

=======
Suggestion 8

def problem158_d():
    s = input()
    q = int(input())
    for i in range(q):
        t = input()
        if t == '1':
            s = s[::-1]
        else:
            f, c = t.split()[1:]
            if f == '1':
                s = c + s
            else:
                s = s + c
    print(s)

=======
Suggestion 9

def main():
    S = input()
    Q = int(input())
    r = False
    for _ in range(Q):
        T, *args = input().split()
        if T == '1':
            r = not r
        else:
            F, C = args
            if F == '1':
                if r:
                    S = S + C
                else:
                    S = C + S
            else:
                if r:
                    S = C + S
                else:
                    S = S + C

    if r:
        S = S[::-1]

    print(S)

=======
Suggestion 10

def reverse(s):
    return s[::-1]
