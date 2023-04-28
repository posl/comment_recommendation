Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            s = s[::-1]
        else:
            if query[1] == '1':
                s = query[2] + s
            else:
                s = s + query[2]
    print(s)

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    reverse = False
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            reverse = not reverse
        else:
            if query[1] == "1":
                if reverse:
                    S = S + query[2]
                else:
                    S = query[2] + S
            else:
                if reverse:
                    S = query[2] + S
                else:
                    S = S + query[2]
    if reverse:
        print(S[::-1])
    else:
        print(S)

=======
Suggestion 3

def main():
    S = input()
    Q = int(input())
    S = list(S)
    reverse = False
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        elif (query[1] == '1') ^ reverse:
            S.insert(0, query[2])
        else:
            S.append(query[2])
    if reverse:
        S.reverse()
    print(''.join(S))

=======
Suggestion 4

def main():
    s = input()
    q = int(input())
    reverse = False
    front = ''
    back = ''
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            if query[1] == '1':
                if reverse:
                    back += query[2]
                else:
                    front += query[2]
            else:
                if reverse:
                    front += query[2]
                else:
                    back += query[2]
    if reverse:
        print(back[::-1] + s[::-1] + front)
    else:
        print(front[::-1] + s + back)

=======
Suggestion 5

def reverse(s):
    return s[::-1]

s = input()
q = int(input())

for i in range(q):
    query = input().split()
    if int(query[0]) == 1:
        s = reverse(s)
    else:
        if int(query[1]) == 1:
            s = query[2] + s
        else:
            s = s + query[2]

print(s)

=======
Suggestion 6

def main():
    s = input()
    q = int(input())
    t = []
    for i in range(q):
        t.append(input().split())
    for i in range(q):
        if t[i][0] == "1":
            s = s[::-1]
        else:
            if t[i][1] == "1":
                s = t[i][2] + s
            else:
                s = s + t[i][2]
    print(s)

=======
Suggestion 7

def main():
    s = input()
    q = int(input())
    s = list(s)
    reverse = False
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            reverse = not reverse
        else:
            if t[1] == '1':
                if reverse:
                    s.append(t[2])
                else:
                    s.insert(0, t[2])
            else:
                if reverse:
                    s.insert(0, t[2])
                else:
                    s.append(t[2])
    if reverse:
        s.reverse()
    print(''.join(s))

=======
Suggestion 8

def main():
    S = input()
    Q = int(input())
    rev = 0
    head = []
    tail = []
    for i in range(Q):
        query = input().split()
        if len(query) == 1:
            rev ^= 1
        else:
            if query[1] == "1":
                if rev == 0:
                    head.append(query[2])
                else:
                    tail.append(query[2])
            else:
                if rev == 0:
                    tail.append(query[2])
                else:
                    head.append(query[2])
    if rev == 0:
        head.reverse()
        print("".join(head) + S + "".join(tail))
    else:
        tail.reverse()
        print("".join(tail)[::-1] + S[::-1] + "".join(head)[::-1])

=======
Suggestion 9

def reverse(s):
    return s[::-1]

s = input()
q = int(input())

for i in range(q):
    query = input()
    if query == '1':
        s = reverse(s)
    else:
        _, f, c = query.split()
        if f == '1':
            s = c + s
        else:
            s = s + c

print(s)

=======
Suggestion 10

def reverse(s):
    return s[::-1]

s = input()
q = int(input())

rev = False
head = ""
tail = ""

for i in range(q):
    t = input().split()
    if t[0] == "1":
        rev = not rev
    else:
        if t[1] == "1":
            if rev:
                tail += t[2]
            else:
                head += t[2]
        else:
            if rev:
                head += t[2]
            else:
                tail += t[2]
