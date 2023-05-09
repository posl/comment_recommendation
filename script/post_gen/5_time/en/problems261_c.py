Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 1
            print(s[i])
        else:
            d[s[i]] += 1
            print(s[i]+'('+str(d[s[i]])+')')

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S.count(S[i]) == 1:
            print(S[i])
        else:
            print(S[i]+'('+str(S[:i].count(S[i]))+')')

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
        else:
            d[S[i]] = 1
        if d[S[i]] == 1:
            print(S[i])
        else:
            print(S[i] + '(' + str(d[S[i]]) + ')')

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] not in s[:i]:
            print(s[i])
        else:
            print(s[i]+"("+str(s[:i].count(s[i]))+")")

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
        else:
            D[S[i]] = 1
        if D[S[i]] == 1:
            print(S[i])
        else:
            print(S[i] + '(' + str(D[S[i]] - 1) + ')')
    return

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for i in range(N):
        if S[i] not in d:
            d[S[i]] = 1
            print(S[i])
        else:
            d[S[i]] += 1
            print(S[i] + "(" + str(d[S[i]]-1) + ")")

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = {}
    for i in range(n):
        if s[i] in t:
            t[s[i]] += 1
            print(s[i] + "(" + str(t[s[i]]) + ")")
        else:
            t[s[i]] = 0
            print(s[i])

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for i in range(N)]
    cnt = {}
    for i in range(N):
        if S[i] not in cnt:
            cnt[S[i]] = 0
        cnt[S[i]] += 1
        if cnt[S[i]] == 1:
            print(S[i])
        else:
            print(S[i] + '(' + str(cnt[S[i]]-1) + ')')

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if i == 0:
            print(s[i])
        else:
            if s[i] in s[:i]:
                cnt = 0
                for j in range(i):
                    if s[j] == s[i]:
                        cnt += 1
                print(s[i] + "(" + str(cnt) + ")")
            else:
                print(s[i])

=======
Suggestion 10

def main():
    N = int(input())
    file_list = []
    for i in range(N):
        file_list.append(input())
    
    file_dict = {}
    for file_name in file_list:
        if file_name in file_dict:
            file_dict[file_name] += 1
        else:
            file_dict[file_name] = 0
        print(file_name + '(' + str(file_dict[file_name]) + ')') if file_dict[file_name] > 0 else print(file_name)
