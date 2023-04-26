Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    reverse = False
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            reverse = not reverse
        elif query[1] == "1":
            if reverse:
                S += query[2]
            else:
                S = query[2] + S
        else:
            if reverse:
                S = query[2] + S
            else:
                S += query[2]
    print(S[::-1] if reverse else S)

=======
Suggestion 2

def main():
    s = input()
    q = int(input())
    ans = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            s = s[::-1]
        else:
            if query[1] == '1':
                s = query[2] + s
            else:
                s += query[2]
    print(s)

=======
Suggestion 3

def main():
    S = input()
    Q = int(input())

    T = []
    F = []
    C = []
    for i in range(Q):
        t = list(map(str, input().split()))
        T.append(t[0])
        if len(t) == 3:
            F.append(t[1])
            C.append(t[2])

    a = []
    b = []
    for i in range(Q):
        if T[i] == "1":
            a, b = b, a
        else:
            if F[i] == "1":
                a.append(C[i])
            else:
                b.append(C[i])

    S = "".join(a[::-1]) + S + "".join(b)
    print(S)

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    ans = []
    for i in range(Q):
        if query[i][0] == "1":
            query = query[::-1]
        else:
            if query[i][1] == "1":
                ans.append(query[i][2])
            else:
                ans.append(query[i][2])
    ans = "".join(ans)
    if query[0][0] == "1":
        ans = ans[::-1]
    ans = ans + S
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    Q = int(input())
    S = list(S)
    reverse = False
    for i in range(Q):
        query = input()
        if query == '1':
            reverse = not reverse
        else:
            query = query.split()
            if query[1] == '1':
                if reverse:
                    S.append(query[2])
                else:
                    S.insert(0, query[2])
            else:
                if reverse:
                    S.insert(0, query[2])
                else:
                    S.append(query[2])
    if reverse:
        S = S[::-1]
    print(''.join(S))

=======
Suggestion 6

def main():
    s = input()
    q = int(input())
    queries = [list(map(str, input().split())) for _ in range(q)]

    is_reverse = False

    for query in queries:
        if query[0] == '1':
            is_reverse = not is_reverse
        else:
            if (query[1] == '1' and not is_reverse) or (query[1] == '2' and is_reverse):
                s = query[2] + s
            else:
                s = s + query[2]

    if is_reverse:
        print(s[::-1])
    else:
        print(s)

=======
Suggestion 7

def main():
    s = input()
    q = int(input())
    query = [input().split() for _ in range(q)]
    reverse = 0
    head = ""
    tail = ""
    for q in query:
        if q[0] == "1":
            reverse = 1 - reverse
        elif q[0] == "2":
            if q[1] == "1":
                if reverse == 0:
                    head = q[2] + head
                else:
                    tail = tail + q[2]
            else:
                if reverse == 0:
                    tail = tail + q[2]
                else:
                    head = q[2] + head
    if reverse == 1:
        print(tail[::-1] + s + head[::-1])
    else:
        print(head + s + tail)

=======
Suggestion 8

def main():
    s = input()
    q = int(input())
    querys = [input().split() for _ in range(q)]
    querys.reverse()
    reverse = False
    for query in querys:
        if query[0] == '1':
            reverse = not reverse
        else:
            if query[1] == '1':
                if reverse:
                    s += query[2]
                else:
                    s = query[2] + s
            else:
                if reverse:
                    s = query[2] + s
                else:
                    s += query[2]
    if reverse:
        s = s[::-1]
    print(s)

=======
Suggestion 9

def main():
    S = input()
    Q = int(input())
    N = len(S)
    rev = 0
    for i in range(Q):
        query = list(map(str, input().split()))
        if len(query) == 1:
            rev += 1
        else:
            if query[1] == '1':
                if rev % 2 == 0:
                    S = query[2] + S
                else:
                    S = S + query[2]
            else:
                if rev % 2 == 0:
                    S = S + query[2]
                else:
                    S = query[2] + S
    if rev % 2 == 1:
        S = S[::-1]
    print(S)

=======
Suggestion 10

def main():
    s = input()
    q = int(input())
    query = [input().split() for _ in range(q)]
    query.reverse()

    ans = list(s)
    reverse = False

    for i in range(q):
        if query[i][0] == '1':
            reverse = not reverse
        else:
            if (query[i][1] == '1' and not reverse) or (query[i][1] == '2' and reverse):
                ans.insert(0, query[i][2])
            else:
                ans.append(query[i][2])

    if reverse:
        ans.reverse()
    print(''.join(ans))
