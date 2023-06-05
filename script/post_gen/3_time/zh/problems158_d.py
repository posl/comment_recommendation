Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    s = input()
    q = int(input())
    query = []
    for i in range(q):
        query.append(input().split())
    reverse = False
    for i in range(q):
        if query[i][0] == '1':
            reverse = not reverse
        elif query[i][0] == '2':
            if query[i][1] == '1':
                if reverse:
                    s += query[i][2]
                else:
                    s = query[i][2] + s
            elif query[i][1] == '2':
                if reverse:
                    s = s + query[i][2]
                else:
                    s = query[i][2] + s
    if reverse:
        s = s[::-1]
    print(s)

=======
Suggestion 3

def reverse(s):
    return s[::-1]

s = input()
q = int(input())
for i in range(q):
    query = input().split()
    if query[0] == '1':
        s = reverse(s)
    elif query[0] == '2':
        if query[1] == '1':
            s = query[2] + s
        elif query[1] == '2':
            s = s + query[2]
print(s)

=======
Suggestion 4

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t = input().split()
        if t[0] == "1":
            s = s[::-1]
        else:
            if t[1] == "1":
                s = t[2] + s
            else:
                s = s + t[2]
    print(s)

=======
Suggestion 5

def func(s, q, query):
    for i in range(q):
        if query[i][0] == 1:
            s = s[::-1]
        elif query[i][0] == 2:
            if query[i][1] == 1:
                s = query[i][2] + s
            elif query[i][1] == 2:
                s = s + query[i][2]
    return s

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def reverse(s):
    return s[::-1]

=======
Suggestion 8

def reverse_str(s):
    return s[::-1]

=======
Suggestion 9

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
Suggestion 10

def main():
    s = input()
    q = int(input())
    s = list(s)
    flag = True
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            flag = not flag
        else:
            if t[1] == '1':
                if flag:
                    s.insert(0, t[2])
                else:
                    s.append(t[2])
            else:
                if flag:
                    s.append(t[2])
                else:
                    s.insert(0, t[2])
    if flag:
        print(''.join(s))
    else:
        print(''.join(s[::-1]))
