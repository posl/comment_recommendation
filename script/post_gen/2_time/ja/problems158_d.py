Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    t = [0] * q
    f = [0] * q
    c = [0] * q
    for i in range(q):
        t[i], f[i], c[i] = input().split()
        t[i] = int(t[i])
        f[i] = int(f[i])
    ans = s
    for i in range(q):
        if t[i] == 1:
            ans = ans[::-1]
        else:
            if f[i] == 1:
                ans = c[i] + ans
            else:
                ans = ans + c[i]
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            s = s[::-1]
        else:
            if t[1] == '1':
                s = t[2] + s
            else:
                s = s + t[2]
    print(s)

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    t = [0]*q
    f = [0]*q
    c = [0]*q
    for i in range(q):
        t[i],f[i],c[i] = map(str,input().split())
    for i in range(q):
        if t[i] == '1':
            s = s[::-1]
        elif t[i] == '2':
            if f[i] == '1':
                s = c[i] + s
            elif f[i] == '2':
                s = s + c[i]
    print(s)

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    reverse = False
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            if reverse:
                if query[1] == '1':
                    S += query[2]
                else:
                    S = query[2] + S
            else:
                if query[1] == '1':
                    S = query[2] + S
                else:
                    S += query[2]
    if reverse:
        S = S[::-1]
    print(S)

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    rev = 0
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            rev = 1 - rev
        else:
            if (query[1] == '1' and rev == 0) or (query[1] == '2' and rev == 1):
                s = query[2] + s
            else:
                s = s + query[2]
    if rev == 1:
        s = s[::-1]
    print(s)

=======
Suggestion 6

def main():
    s = input()
    q = int(input())
    is_reverse = False
    front = ''
    back = ''
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            is_reverse = not is_reverse
        else:
            if query[1] == '1':
                if is_reverse:
                    back += query[2]
                else:
                    front += query[2]
            else:
                if is_reverse:
                    front += query[2]
                else:
                    back += query[2]
    if is_reverse:
        print(back[::-1] + s[::-1] + front)
    else:
        print(front[::-1] + s + back)

=======
Suggestion 7

def main():
    s = list(input())
    q = int(input())

    reverse = False
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            if query[1] == '1':
                if reverse:
                    s.append(query[2])
                else:
                    s.insert(0, query[2])
            else:
                if reverse:
                    s.insert(0, query[2])
                else:
                    s.append(query[2])
    if reverse:
        s.reverse()
    print(''.join(s))

=======
Suggestion 8

def main():
    S = input()
    Q = int(input())
    S = list(S)
    flag = 0
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            if flag == 0:
                flag = 1
            else:
                flag = 0
        else:
            if query[1] == '1':
                if flag == 0:
                    S.insert(0, query[2])
                else:
                    S.append(query[2])
            else:
                if flag == 0:
                    S.append(query[2])
                else:
                    S.insert(0, query[2])
    if flag == 0:
        print(''.join(S))
    else:
        print(''.join(S[::-1]))

=======
Suggestion 9

def main():
    s = input()
    q = int(input())
    rev = False
    head = []
    tail = []
    for i in range(q):
        t = list(input().split())
        if t[0] == "1":
            rev = not rev
        else:
            if t[1] == "1":
                if rev:
                    tail.append(t[2])
                else:
                    head.append(t[2])
            else:
                if rev:
                    head.append(t[2])
                else:
                    tail.append(t[2])
    if rev:
        print("".join(tail[::-1]) + s[::-1] + "".join(head))
    else:
        print("".join(head[::-1]) + s + "".join(tail))

=======
Suggestion 10

def main():
    # input
    S = input()
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(input().split())

    # compute
    forward = True
    for i in range(Q):
        if Query[i][0] == '1':
            forward = not forward
        elif Query[i][1] == '1':
            if forward:
                S = Query[i][2] + S
            else:
                S = S + Query[i][2]
        else:
            if forward:
                S = S + Query[i][2]
            else:
                S = Query[i][2] + S

    # output
    if forward:
        print(S)
    else:
        print(S[::-1])
