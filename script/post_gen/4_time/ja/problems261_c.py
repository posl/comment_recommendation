Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    dic = {}
    for s in S:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
        print(s if dic[s] == 1 else s + '(' + str(dic[s] - 1) + ')')

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            print(s[i]+'('+str(d[s[i]])+')')
        else:
            d[s[i]] = 0
            print(s[i])

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    D = {}
    for s in S:
        if s in D:
            D[s] += 1
        else:
            D[s] = 1
        if D[s] == 1:
            print(s)
        else:
            print(s + '(' + str(D[s]) + ')')

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
        else:
            d[S[i]] = 1
        print(S[i] if d[S[i]] == 1 else S[i] + '(' + str(d[S[i]]) + ')')

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    cnt = {}
    for s in S:
        if s not in cnt:
            cnt[s] = 1
        else:
            cnt[s] += 1
    ans = []
    for i in range(N):
        if cnt[S[i]] == 1:
            ans.append(S[i])
        else:
            ans.append(S[i] + "(" + str(cnt[S[i]] - 1) + ")")
    print("\n".join(ans))

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    memo = {}
    for i in range(n):
        if s[i] in memo:
            memo[s[i]] += 1
            print(s[i] + '(' + str(memo[s[i]] - 1) + ')')
        else:
            memo[s[i]] = 1
            print(s[i])

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for i in range(n)]
    cnt = {}
    for i in range(n):
        if s[i] not in cnt:
            cnt[s[i]] = 0
            print(s[i])
        else:
            cnt[s[i]] += 1
            print(s[i] + '(' + str(cnt[s[i]]) + ')')

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    S_dict = {}
    for i in range(N):
        if S[i] not in S_dict:
            S_dict[S[i]] = 1
            print(S[i])
        else:
            S_dict[S[i]] += 1
            print(S[i]+"("+str(S_dict[S[i]]-1)+")")

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(S)
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]] += 1
        else:
            d[S[i]] = 1
        if d[S[i]] == 1:
            print(S[i])
        else:
            print(S[i] + "(" + str(d[S[i]]) + ")")

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s_set = set(s)
    s_dict = {}
    for i in range(n):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
            print(s[i])
        else:
            s_dict[s[i]] += 1
            print(s[i] + "(" + str(s_dict[s[i]] - 1) + ")")
