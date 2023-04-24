Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        T = list(map(str, input().split()))
        if T[0] == '1':
            S = S[::-1]
        elif T[0] == '2':
            if T[1] == '1':
                S = T[2] + S
            elif T[1] == '2':
                S = S + T[2]
    print(S)

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    rev = False
    head = []
    tail = []
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            rev = not rev
        else:
            if query[1] == "1":
                if not rev:
                    head.append(query[2])
                else:
                    tail.append(query[2])
            else:
                if not rev:
                    tail.append(query[2])
                else:
                    head.append(query[2])
    if rev:
        head, tail = tail, head
    print("".join(head[::-1]) + S + "".join(tail))

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    for i in range(q):
        query = list(map(str,input().split()))
        if query[0] == '1':
            s = s[::-1]
        else:
            if query[1] == '1':
                s = query[2] + s
            else:
                s = s + query[2]
    print(s)

=======
Suggestion 4

def main():
    s = input()
    q = int(input())
    t = []
    f = []
    c = []
    for i in range(q):
        t.append(int(input()))
        if t[i] == 2:
            f.append(int(input()))
            c.append(input())
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
Suggestion 5

def main():
    s = input()
    q = int(input())
    rev = 0
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            rev ^= 1
        else:
            if (int(query[1]) ^ rev) == 0:
                s = query[2] + s
            else:
                s = s + query[2]
    if rev == 1:
        s = s[::-1]
    print(s)

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    query = [list(map(str, input().split())) for _ in range(Q)]
    ans = []
    for i in range(Q):
        if query[i][0] == '1':
            S = S[::-1]
        elif query[i][0] == '2':
            if query[i][1] == '1':
                S = query[i][2] + S
            elif query[i][1] == '2':
                S = S + query[i][2]
    print(S)

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    reverse = False
    front = []
    back = []
    for q in query:
        if q[0] == '1':
            reverse = not reverse
        else:
            if q[1] == '1':
                if reverse:
                    back.append(q[2])
                else:
                    front.append(q[2])
            else:
                if reverse:
                    front.append(q[2])
                else:
                    back.append(q[2])
    if reverse:
        front, back = back[::-1], front[::-1]
    print(''.join(front + list(S) + back))

=======
Suggestion 8

def main():
    S = input()
    Q = int(input())
    rev = False
    front = []
    back = []
    for _ in range(Q):
        q = list(input().split())
        if q[0] == "1":
            rev = not rev
        else:
            if q[1] == "1":
                if rev:
                    back.append(q[2])
                else:
                    front.append(q[2])
            else:
                if rev:
                    front.append(q[2])
                else:
                    back.append(q[2])
    if rev:
        print("".join(list(reversed(front))+list(reversed(S))+list(reversed(back))))
    else:
        print("".join(front+S+back))

=======
Suggestion 9

def main():
    S = input()
    Q = int(input())
    query = [list(map(str, input().split())) for _ in range(Q)]
    flag = 0
    for q in query:
        if q[0] == "1":
            flag = 1 - flag
        else:
            if (q[1] == "1" and flag == 0) or (q[1] == "2" and flag == 1):
                S = q[2] + S
            else:
                S = S + q[2]
    if flag == 1:
        S = S[::-1]
    print(S)

=======
Suggestion 10

def main():
    S = list(input())
    Q = int(input())
    t = []
    f = []
    c = []
    for _ in range(Q):
        T = input().split()
        t.append(T[0])
        if len(T) == 3:
            f.append(T[1])
            c.append(T[2])
    #print(S)
    #print(Q)
    #print(t)
    #print(f)
    #print(c)
    rev = 0
    for i in range(Q):
        if t[i] == '1':
            rev += 1
        else:
            if (int(f[i]) + rev) % 2 == 0:
                S.append(c[i])
            else:
                S.insert(0, c[i])
    #print(S)
    if rev % 2 == 0:
        print(''.join(S))
    else:
        print(''.join(reversed(S)))
