Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s not in d:
            d[s] = 1
            print(s)
        else:
            print(s + '(' + str(d[s]) + ')')
            d[s] += 1

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
            print(S[i] + "(" + str(D[S[i]]) + ")")
        else:
            D[S[i]] = 0
            print(S[i])

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for i in range(n)]
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 1
            print(s[i])
        else:
            print(s[i] + "(" + str(d[s[i]]) + ")")
            d[s[i]] += 1

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for i in range(N)]
    d = {}
    for i in range(N):
        if S[i] not in d:
            d[S[i]] = 1
            print(S[i])
        else:
            print(S[i] + "(" + str(d[S[i]]) + ")")
            d[S[i]] += 1

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = []
    for i in range(N):
        if S[i] not in S[:i]:
            ans.append(S[i])
        else:
            X = S[:i].count(S[i])
            ans.append(S[i] + "(" + str(X) + ")")
    for i in range(N):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_dic = {}
    for i in range(N):
        if S[i] in S_dic:
            S_dic[S[i]] += 1
            print(S[i] + "(" + str(S_dic[S[i]]) + ")")
        else:
            S_dic[S[i]] = 0
            print(S[i])

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = []
    for s in S:
        if s in ans:
            ans.append(s + '(' + str(ans.count(s)) + ')')
        else:
            ans.append(s)
    for a in ans:
        print(a)

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    for i in range(N):
        if S[i] in S[:i]:
            count = 0
            for j in range(i):
                if S[i] == S[j]:
                    count += 1
            print(S[i] + '(' + str(count) + ')')
        else:
            print(S[i])

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = []
    for i in range(N):
        if S[i] in ans:
            cnt = 0
            for j in range(i):
                if S[i] == S[j]:
                    cnt += 1
            ans.append(S[i] + "(" + str(cnt) + ")")
        else:
            ans.append(S[i])
    for i in range(N):
        print(ans[i])

=======
Suggestion 10

def main():
    N = int(input())
    str_list = []
    for i in range(N):
        str_list.append(input())
    for i in range(N):
        if str_list.count(str_list[i]) > 1:
            print(str_list[i] + "(" + str(str_list.count(str_list[i])-1) + ")")
        else:
            print(str_list[i])
