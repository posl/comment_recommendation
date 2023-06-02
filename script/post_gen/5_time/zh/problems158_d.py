Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t = input().split()
        if len(t) == 1:
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
Suggestion 2

def problem158_d():
    pass

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    reverse = False
    head = ''
    tail = ''
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            if query[1] == '1':
                if reverse:
                    tail += query[2]
                else:
                    head += query[2]
            else:
                if reverse:
                    head += query[2]
                else:
                    tail += query[2]
    if reverse:
        head, tail = tail[::-1], head[::-1]
    print(head + s + tail)

=======
Suggestion 4

def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = 0
    for i in range(q):
        t = list(map(str, input().split()))
        if t[0] == '1':
            rev = 1 - rev
        else:
            if t[1] == '1':
                if rev == 0:
                    s.insert(0, t[2])
                else:
                    s.append(t[2])
            else:
                if rev == 0:
                    s.append(t[2])
                else:
                    s.insert(0, t[2])
    if rev == 1:
        s.reverse()
    print(''.join(s))

=======
Suggestion 5

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
Suggestion 6

def main():
    # 读入输入
    s = list(input())
    q = int(input())
    # 倒序标志
    rev = 0
    # 从后向前读入
    for i in range(q):
        tmp = input().split()
        # 反转
        if tmp[0] == '1':
            rev = 1 - rev
        # 添加
        else:
            f = int(tmp[1])
            c = tmp[2]
            if (f == 1 and rev == 0) or (f == 2 and rev == 1):
                s.insert(0, c)
            else:
                s.append(c)
    # 结果
    if rev == 1:
        s.reverse()
    print(''.join(s))

=======
Suggestion 7

def main():
    s = input().strip()
    q = int(input().strip())
    reverse = False
    head = ''
    tail = ''
    for _ in range(q):
        query = input().strip().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            f = query[1]
            c = query[2]
            if f == '1':
                if reverse:
                    tail += c
                else:
                    head += c
            else:
                if reverse:
                    head += c
                else:
                    tail += c
    res = head + s + tail
    if reverse:
        res = res[::-1]
    print(res)

=======
Suggestion 8

def reverse(s):
    return s[::-1]

=======
Suggestion 9

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
Suggestion 10

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
