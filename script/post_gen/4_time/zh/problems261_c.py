Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    return N,S

=======
Suggestion 2

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
            print(s + "(" + str(d[s]) + ")")
        else:
            d[s] = 0
            print(s)

=======
Suggestion 3

def solve():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
            print(s + '(' + str(d[s]) + ')')
        else:
            d[s] = 0
            print(s)

=======
Suggestion 4

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    count = {}
    for i in range(n):
        if a[i] not in count:
            count[a[i]] = 0
            print(a[i])
        else:
            count[a[i]] += 1
            print(a[i] + '(' + str(count[a[i]]) + ')')

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    for i in range(N):
        if i == 0:
            print(S[i])
        else:
            if S[i] in S[:i]:
                cnt = S[:i].count(S[i])
                print(S[i] + "(" + str(cnt) + ")")
            else:
                print(S[i])

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S[i] not in S[:i]:
            print(S[i])
        else:
            cnt = S[:i].count(S[i])
            print(S[i]+'('+str(cnt)+')')

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] not in s[:i]:
            print(s[i])
        else:
            x = s[:i].count(s[i])
            print(s[i]+"("+str(x)+")")

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s2 = []
    for i in range(n):
        if s[i] in s2:
            cnt = 1
            for j in range(len(s2)):
                if s[i] == s2[j]:
                    cnt += 1
            s2.append(s[i] + "(" + str(cnt) + ")")
        else:
            s2.append(s[i])
    for i in range(len(s2)):
        print(s2[i])

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S[i] not in S[:i]:
            print(S[i])
        else:
            j = S[:i].count(S[i])
            print(S[i] + "(" + str(j+1) + ")")

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s.count(s[i]) == 1:
            print(s[i])
        else:
            print(s[i] + "(" + str(s[:i].count(s[i])) + ")")
