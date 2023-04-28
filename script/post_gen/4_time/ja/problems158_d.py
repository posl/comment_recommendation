Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    s = input()
    q = int(input())
    rev = False
    head = ''
    tail = ''
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            rev = not rev
        else:
            if query[1] == '1':
                if rev:
                    tail += query[2]
                else:
                    head += query[2]
            else:
                if rev:
                    head += query[2]
                else:
                    tail += query[2]
    if rev:
        s = s[::-1]
        head = head[::-1]
        tail = tail[::-1]
    print(head + s + tail)

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())

    for i in range(q):
        if query[i][0] == '1':
            s = s[::-1]
        else:
            if query[i][1] == '1':
                s = query[i][2] + s
            else:
                s = s + query[i][2]

    print(s)

=======
Suggestion 4

def reverse(s):
    return s[::-1]

s = input()
q = int(input())

head = ''
tail = ''

for i in range(q):
    query = input().split()
    if query[0] == '1':
        head, tail = tail, head
    else:
        if query[1] == '1':
            head = query[2] + head
        else:
            tail += query[2]

print(reverse(head) + s + tail)

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for i in range(q):
        query = input().split()
        t = int(query[0])
        if t == 1:
            rev = not rev
        else:
            f = int(query[1])
            c = query[2]
            if f == 1:
                if rev:
                    s.append(c)
                else:
                    s.insert(0, c)
            else:
                if rev:
                    s.insert(0, c)
                else:
                    s.append(c)
    if rev:
        s.reverse()
    print("".join(s))

=======
Suggestion 6

def main():
    s = input()
    q = int(input())
    s = list(s)
    reverse = False
    for i in range(q):
        t = list(map(str, input().split()))
        if t[0] == "1":
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
    print("".join(s))

=======
Suggestion 7

def main():
    s = input()
    q = int(input())
    t = []
    for i in range(q):
        t.append(input().split())

    head = ''
    tail = ''
    for i in range(q):
        if t[i][0] == '1':
            if head == '':
                head = s
            else:
                head, tail = tail, head
        else:
            if t[i][1] == '1':
                head = t[i][2] + head
            else:
                tail += t[i][2]

    if head == '':
        print(s + tail)
    else:
        print(head + s + tail)

=======
Suggestion 8

def main():
    s = input()
    q = int(input())
    ans = s
    reverse = False
    for _ in range(q):
        t = input()
        if t == '1':
            reverse = not reverse
        else:
            _, f, c = t.split()
            if (f == '1') ^ reverse:
                ans = c + ans
            else:
                ans = ans + c

    if reverse:
        ans = ans[::-1]

    print(ans)

=======
Suggestion 9

def main():
    s = input()
    q = int(input())
    s = list(s)
    head = []
    tail = []
    reverse = False
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            reverse = not reverse
        else:
            if query[1] == "1":
                if reverse:
                    tail.append(query[2])
                else:
                    head.append(query[2])
            else:
                if reverse:
                    head.append(query[2])
                else:
                    tail.append(query[2])
    if reverse:
        s = s[::-1]
        tail = tail[::-1]
        head = head[::-1]
    ans = "".join(head) + "".join(s) + "".join(tail)
    print(ans)

=======
Suggestion 10

def reverse(s):
    return s[::-1]
