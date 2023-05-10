Synthesizing 10/10 solutions

=======
Suggestion 1

def replaceABC(s):
    s = s.replace("A","BC")
    s = s.replace("B","CA")
    s = s.replace("C","AB")
    return s

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    for t, k in query:
        t %= 3
        if t == 0:
            print(S[k-1])
        elif t == 1:
            print(S[k-1].translate(str.maketrans('ABC', 'BCA')))
        else:
            print(S[k-1].translate(str.maketrans('ABC', 'CAB')))

=======
Suggestion 3

def f(s):
    return s.replace('A','BC').replace('B','CA').replace('C','AB')

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    lst = []
    for i in range(Q):
        t, k = map(int, input().split())
        lst.append((t, k))
    #print(lst)
    for i in range(Q):
        t, k = lst[i]
        t = t % 3
        #print(t, k)
        if t == 0:
            print(S[k-1])
        elif t == 1:
            if k <= len(S):
                print(S[k-1])
            else:
                print(S[k-1 - len(S)])
        else:
            if k <= len(S):
                print(S[k-1])
            else:
                print(S[k-1 - len(S) * 2])

=======
Suggestion 5

def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        t = t % 3
        k = k - 1
        for _ in range(t):
            S = S.replace("A", "BC")
            S = S.replace("B", "CA")
            S = S.replace("C", "AB")
        print(S[k])

=======
Suggestion 6

def replace(s):
    i = 0
    r = ''
    while i < len(s):
        if s[i] == 'A':
            r = r + 'BC'
        elif s[i] == 'B':
            r = r + 'CA'
        else:
            r = r + 'AB'
        i = i + 1
    return r

s = input()
q = int(input())

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    for t, k in queries:
        t -= 1
        while t > 0:
            if k <= len(S):
                if S[k - 1] == 'A':
                    S = 'BC' + S[k:]
                elif S[k - 1] == 'B':
                    S = 'CA' + S[k:]
                else:
                    S = 'AB' + S[k:]
                break
            else:
                t -= 1
                k -= len(S)
        print(S[k - 1])

=======
Suggestion 8

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        t = t % 3
        for j in range(t):
            s = s.replace('A', 'BC')
            s = s.replace('B', 'CA')
            s = s.replace('C', 'AB')
        print(s[k-1])

=======
Suggestion 9

def replace(S):
    S = S.replace('A', 'BC')
    S = S.replace('B', 'CA')
    S = S.replace('C', 'AB')
    return S

S = input()
Q = int(input())
query = []
for _ in range(Q):
    t, k = map(int, input().split())
    query.append((t, k))

for t, k in query:
    if t == 0:
        print(S[k-1])
    else:
        S = replace(S)
        print(S[k-1])

=======
Suggestion 10

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int,input().split())
        for j in range(t):
            s = s.replace('A','BC')
            s = s.replace('B','CA')
            s = s.replace('C','AB')
        print(s[k-1])
