Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s not in d:
            d[s] = 0
            print(s)
        else:
            d[s] += 1
            print(s + '(' + str(d[s]) + ')')

main()

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = {}
    for s in S:
        if s not in D:
            D[s] = 0
            print(s)
        else:
            D[s] += 1
            print(s + '(' + str(D[s]) + ')')

=======
Suggestion 3

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
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
            print(s + '(' + str(d[s]) + ')')
        else:
            d[s] = 0
            print(s)

=======
Suggestion 5

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
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    cnt = {}
    for i in range(N):
        if S[i] in cnt:
            cnt[S[i]] += 1
            S[i] += '(' + str(cnt[S[i]]) + ')'
        else:
            cnt[S[i]] = 0
    for i in range(N):
        print(S[i])

=======
Suggestion 7

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
            count = 1
            for j in range(i-1,-1,-1):
                if S[i] == S[j]:
                    count += 1
                else:
                    break
            ans.append(S[i] + '(' + str(count-1) + ')')
    for i in range(N):
        print(ans[i])

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S_dict = {}
    for i in range(N):
        if S[i] in S_dict:
            S_dict[S[i]] += 1
            print(S[i] + "(" + str(S_dict[S[i]]) + ")")
        else:
            S_dict[S[i]] = 0
            print(S[i])
    return 0

=======
Suggestion 9

def main():
    import sys
    N = int(sys.stdin.readline())
    S = [sys.stdin.readline().rstrip() for _ in range(N)]
    D = {}
    for i in range(N):
        if S[i] in D:
            D[S[i]] += 1
            S[i] += "({})".format(D[S[i]])
        else:
            D[S[i]] = 0
    print(*S, sep = "

")

=======
Suggestion 10

def main():
    import sys
    from collections import Counter

    N = int(sys.stdin.readline())
    S = [sys.stdin.readline().rstrip() for _ in range(N)]
    C = Counter(S)

    for s in S:
        if C[s] == 1:
            print(s)
        else:
            print(s + '(' + str(C[s] - 1) + ')')
            C[s] -= 1
