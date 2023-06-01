Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def reverse_string(s):
    return s[::-1]

=======
Suggestion 2

def main():
    s = input()
    q = int(input())
    t = []
    f = []
    c = []
    for i in range(q):
        t_i = input().split()
        t.append(int(t_i[0]))
        if t_i[0] == '2':
            f.append(int(t_i[1]))
            c.append(t_i[2])
    #print(s)
    #print(q)
    #print(t)
    #print(f)
    #print(c)
    for i in range(q):
        if t[i] == 1:
            s = s[::-1]
        else:
            if f[i] == 1:
                s = c[i] + s
            else:
                s = s + c[i]
    print(s)

=======
Suggestion 3

def reverse(s):
    return s[::-1]

=======
Suggestion 4

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            s = s[::-1]
        else:
            f = int(t[1])
            c = t[2]
            if f == 1:
                s = c + s
            else:
                s = s + c
    print(s)

=======
Suggestion 5

def reverse(s):
    return s[::-1]

S = input().strip()
Q = int(input())
s = S
for i in range(Q):
    query = input().strip().split()
    if query[0] == '1':
        s = reverse(s)
    else:
        if query[1] == '1':
            s = query[2] + s
        else:
            s = s + query[2]
print(s)

=======
Suggestion 6

def main():
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
Suggestion 7

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        query = input()
        if query == '1':
            S = S[::-1]
        else:
            T_i, F_i, C_i = query.split()
            if F_i == '1':
                S = C_i + S
            else:
                S = S + C_i
    print(S)

=======
Suggestion 8

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
