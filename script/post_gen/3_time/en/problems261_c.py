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
            d[s[i]] = 0
            print(s[i])
        else:
            d[s[i]] += 1
            print(s[i] + "(" + str(d[s[i]]) + ")")

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 0
            print(s[i])
        else:
            d[s[i]] += 1
            print(s[i] + '({})'.format(d[s[i]]))
    return

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = {}
    for s in S:
        if s in D:
            D[s] += 1
            print(s + '(' + str(D[s]) + ')')
        else:
            D[s] = 0
            print(s)

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for i in range(N)]
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
            print(S[i] + '(' + str(D[S[i]]) + ')')
        else:
            D[S[i]] = 0
            print(S[i])

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    count = {}
    for s in S:
        if s not in count:
            count[s] = 1
            print(s)
        else:
            print(s + '(' + str(count[s]) + ')')
            count[s] += 1

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = []
    for s in S:
        if s not in T:
            T.append(s)
            print(s)
        else:
            print(s + '(' + str(T.count(s)) + ')')
            T.append(s)

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    cnt = {}
    for s in S:
        if s in cnt:
            cnt[s] += 1
            print(s+'('+str(cnt[s])+')')
        else:
            cnt[s] = 0
            print(s)

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ans = [0] * n
    for i in range(n):
        for j in range(i):
            if s[i] == s[j]:
                ans[i] = ans[j] + 1
                break
    for i in range(n):
        if ans[i] == 0:
            print(s[i])
        else:
            print(s[i] + "(" + str(ans[i]) + ")")

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s2 = []
    for i in range(n):
        s2.append(s[i])
    for i in range(n):
        if s2.count(s[i]) == 1:
            print(s[i])
        else:
            for j in range(1, s2.count(s[i]) + 1):
                if s[i] not in s2[j:]:
                    print(s[i])
                else:
                    print(s[i] + "(" + str(j) + ")")
                    s2[j] = s[i] + "(" + str(j) + ")"

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(S)
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
            S[i] = S[i] + '(' + str(D[S[i]]) + ')'
        else:
            D[S[i]] = 0
    for i in range(N):
        print(S[i])

main()
