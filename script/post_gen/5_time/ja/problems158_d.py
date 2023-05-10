Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    s = list(s)
    f = 0
    for i in range(q):
        if query[i][0] == "1":
            if f == 0:
                f = 1
            else:
                f = 0
        else:
            if query[i][1] == "1":
                if f == 0:
                    s.insert(0, query[i][2])
                else:
                    s.append(query[i][2])
            else:
                if f == 0:
                    s.append(query[i][2])
                else:
                    s.insert(0, query[i][2])
    if f == 0:
        print("".join(s))
    else:
        s.reverse()
        print("".join(s))
main()

=======
Suggestion 2

def solve():
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
        print(tail[::-1]+s[::-1]+head)
    else:
        print(head[::-1]+s+tail)

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    ans = s
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            ans = ans[::-1]
        else:
            if t[1] == '1':
                ans = t[2] + ans
            else:
                ans = ans + t[2]
    print(ans)
main()

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
        elif query[1] == '1':
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
Suggestion 5

def main():
    s = input()
    q = int(input())
    rev = False
    head = ''
    tail = ''
    for _ in range(q):
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
        head, tail = tail[::-1], head[::-1]
    print(head + s + tail)

=======
Suggestion 6

def main():
    s = input()
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    for i in range(q):
        if query[i][0] == '1':
            s = s[::-1]
        elif query[i][0] == '2':
            if query[i][1] == '1':
                s = query[i][2] + s
            elif query[i][1] == '2':
                s = s + query[i][2]
    print(s)

=======
Suggestion 7

def main():
    s = input()
    q = int(input())
    t = [0] * q
    f = [0] * q
    c = [0] * q
    for i in range(q):
        t[i], f[i], c[i] = map(str, input().split())
        t[i] = int(t[i])
        f[i] = int(f[i])
    #print(s, q, t, f, c)
    s = list(s)
    #print(s)
    rev = False
    for i in range(q):
        if t[i] == 1:
            rev = not rev
            #print("rev")
        else:
            if f[i] == 1:
                if rev:
                    s.append(c[i])
                else:
                    s.insert(0, c[i])
            else:
                if rev:
                    s.insert(0, c[i])
                else:
                    s.append(c[i])
            #print("add", s)
    if rev:
        s = s[::-1]
    print("".join(s))

=======
Suggestion 8

def main():
    # data load
    s = input()
    q = int(input())
    # print(s)
    # print(q)
    # print(q_list)
    # print(f_list)
    # print(c_list)
    # print(t_list)

    # main
    reverse_count = 0
    reverse_flag = False
    front_flag = True
    s_list = list(s)
    for i in range(q):
        q_list = input().split()
        # print(q_list)
        if q_list[0] == "1":
            if reverse_flag:
                reverse_flag = False
            else:
                reverse_flag = True
        elif q_list[0] == "2":
            if q_list[1] == "1":
                if reverse_flag:
                    s_list.append(q_list[2])
                else:
                    s_list.insert(0, q_list[2])
            elif q_list[1] == "2":
                if reverse_flag:
                    s_list.insert(0, q_list[2])
                else:
                    s_list.append(q_list[2])
        # print(s_list)
    if reverse_flag:
        s_list.reverse()
    print("".join(s_list))

=======
Suggestion 9

def main():
    s = input()
    q = int(input())
    s = list(s)
    reverse = False
    for i in range(q):
        query = input()
        if query[0] == '1':
            reverse = not reverse
        else:
            t, f, c = query.split()
            if reverse:
                f = '1' if f == '2' else '2'
            if f == '1':
                s.insert(0, c)
            else:
                s.append(c)
    if reverse:
        s = s[::-1]
    print(''.join(s))

=======
Suggestion 10

def main():
    s = input()
    q = int(input())
    t = [0] * q
    f = [0] * q
    c = [0] * q
    for i in range(q):
        t[i], f[i], c[i] = map(str, input().split())
        t[i] = int(t[i])
        f[i] = int(f[i])
    s = list(s)
    for i in range(q):
        if t[i] == 1:
            s.reverse()
        elif t[i] == 2:
            if f[i] == 1:
                s.insert(0, c[i])
            elif f[i] == 2:
                s.append(c[i])
    print(''.join(s))
