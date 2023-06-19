Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def reverse(s):
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
        t1 = input().split()
        t.append(int(t1[0]))
        if t1[0] == '2':
            f.append(int(t1[1]))
            c.append(t1[2])
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
        #print(s)
    print(s)

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t = input()
        if t == '1':
            s = s[::-1]
        else:
            f,c = t.split()[1:]
            if f == '1':
                s = c + s
            else:
                s = s + c
    print(s)

=======
Suggestion 4

def main():
    s = raw_input()
    q = int(raw_input())
    query = []
    for i in range(q):
        query.append(raw_input().split())

    for i in range(q):
        if query[i][0] == '1':
            s = s[::-1]
        else:
            if query[i][1] == '1':
                s = query[i][2] + s
            else:
                s = s + query[i][2]
    print s

=======
Suggestion 5

def reverse(s):
    return s[::-1]

s = input()
q = int(input())

for i in range(q):
    t = input().split()
    if t[0] == '1':
        s = reverse(s)
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
    string = input()
    Q = int(input())
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            string = string[::-1]
        else:
            if query[1] == '1':
                string = query[2] + string
            else:
                string = string + query[2]
    print(string)
