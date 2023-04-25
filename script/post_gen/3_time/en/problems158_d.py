Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        T = input().split()
        if T[0] == '1':
            S = S[::-1]
        else:
            if T[1] == '1':
                S = T[2] + S
            else:
                S = S + T[2]
    print(S)

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
    s = list(s)
    for i in range(q):
        if t[i] == 1:
            s.reverse()
        else:
            if f[i] == 1:
                s.insert(0, c[i])
            else:
                s.append(c[i])
    print(''.join(s))

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    reverse = False
    for _ in range(q):
        t = input().split()
        if t[0] == '1':
            reverse = not reverse
        else:
            if t[1] == '1':
                if reverse:
                    s = s + t[2]
                else:
                    s = t[2] + s
            else:
                if reverse:
                    s = t[2] + s
                else:
                    s = s + t[2]
    if reverse:
        s = s[::-1]
    print(s)

=======
Suggestion 4

def main():
    s = input()
    q = int(input())
    rev = False
    head = []
    tail = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            rev = not rev
        else:
            if query[1] == '1':
                if rev:
                    tail.append(query[2])
                else:
                    head.append(query[2])
            else:
                if rev:
                    head.append(query[2])
                else:
                    tail.append(query[2])
    if rev:
        head.reverse()
        head = ''.join(head)
        s = s[::-1]
        print(head + s + ''.join(tail))
    else:
        tail.reverse()
        tail = ''.join(tail)
        print(tail + s + ''.join(head))

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            rev = not rev
        else:
            if (t[1] == '1') ^ rev:
                s.insert(0, t[2])
            else:
                s.append(t[2])
    if rev:
        s.reverse()
    print(''.join(s))

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    rev = False
    head = ""
    tail = ""
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            rev = not rev
        else:
            if (query[1] == "1" and not rev) or (query[1] == "2" and rev):
                head += query[2]
            else:
                tail += query[2]
    if rev:
        print(tail[::-1] + S[::-1] + head)
    else:
        print(head[::-1] + S + tail)

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    reverse = False
    head = []
    tail = []
    for i in range(Q):
        query = input()
        if query == '1':
            reverse = not reverse
        else:
            _, f, c = query.split()
            if f == '1':
                if reverse:
                    tail.append(c)
                else:
                    head.append(c)
            else:
                if reverse:
                    head.append(c)
                else:
                    tail.append(c)
    if reverse:
        print(''.join(tail[::-1]) + S[::-1] + ''.join(head))
    else:
        print(''.join(head[::-1]) + S + ''.join(tail))

=======
Suggestion 8

def reverse(s):
  return s[::-1]

s = input()
q = int(input())

t = [0] * q
f = [0] * q
c = [0] * q

for i in range(q):
  t[i] = input().split()
  if t[i][0] == '2':
    f[i] = int(t[i][1])
    c[i] = t[i][2]

for i in range(q):
  if t[i][0] == '1':
    s = reverse(s)
  else:
    if f[i] == 1:
      s = c[i] + s
    else:
      s = s + c[i]

print(s)

=======
Suggestion 9

def main():
    s = input()
    q = int(input())
    r = 0
    for i in range(q):
        t = input()
        if t == "1":
            r += 1
        else:
            t,f,c = t.split()
            if f == "1":
                if r % 2 == 0:
                    s = c + s
                else:
                    s = s + c
            else:
                if r % 2 == 0:
                    s = s + c
                else:
                    s = c + s
    if r % 2 == 1:
        s = s[::-1]
    print(s)

=======
Suggestion 10

def reverseString(s):
    return ''.join(reversed(s))
