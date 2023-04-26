Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            print(s[i] + "(" + str(d[s[i]]) + ")")
        else:
            d[s[i]] = 0
            print(s[i])

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
            print(S[i] + '(' + str(d[S[i]]) + ')')
        else:
            d[S[i]] = 0
            print(S[i])

=======
Suggestion 3

def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            print(s[i] + '(' + str(d[s[i]]-1) + ')')
        else:
            d[s[i]] = 1
            print(s[i])

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dic = {}
    for i in range(N):
        if S[i] not in dic:
            dic[S[i]] = 1
            print(S[i])
        else:
            dic[S[i]] += 1
            print(S[i]+"("+str(dic[S[i]]-1)+")")

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for i in range(N)]
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
            print(S[i] + "(" + str(D[S[i]]) + ")")
        else:
            D[S[i]] = 0
            print(S[i])

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    dic = {}
    for i in range(n):
        if s[i] in dic:
            dic[s[i]] += 1
            print(s[i] + '(' + str(dic[s[i]]-1) + ')')
        else:
            dic[s[i]] = 1
            print(s[i])

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = []
    for i in range(N):
        if S[i] not in ans:
            ans.append(S[i])
            print(S[i])
        else:
            num = ans.count(S[i])
            ans.append(S[i])
            print(S[i] + '(' + str(num) + ')')

=======
Suggestion 8

def main():
    n = int(input())
    file_dict = {}
    for i in range(n):
        file_name = input()
        if file_name in file_dict:
            file_dict[file_name] += 1
            print(file_name + "(" + str(file_dict[file_name]) + ")")
        else:
            file_dict[file_name] = 0
            print(file_name)

=======
Suggestion 9

def main():
    N=int(input())
    S=[input() for i in range(N)]
    d={}
    for s in S:
        if s in d:
            d[s]+=1
        else:
            d[s]=1
    for s in S:
        if d[s]==1:
            print(s)
        else:
            print(s+"("+str(d[s]-1)+")")

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S2 = []
    S3 = []
    for i in range(N):
        if S[i] not in S2:
            S2.append(S[i])
            S3.append(0)
        else:
            S3[S2.index(S[i])] += 1
            S2.append(S[i])
            S3.append(0)
    for i in range(N):
        if S3[S2.index(S[i])] == 0:
            print(S[i])
        else:
            print(S[i] + '(' + str(S3[S2.index(S[i])]) + ')')
