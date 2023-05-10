Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #N,M = map(int,input().split())
    #S = [input() for i in range(N)]
    #T = [input() for i in range(M)]
    N,M = 4,4
    S = ['ab','cd','ef','gh']
    T = ['hoge','fuga','____','_ab_cd_ef_gh_']
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                print(-1)
                return
    print('ab__ef___cd_gh')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    if N == 1 and M == 1:
        if S[0] == T[0]:
            print(-1)
        else:
            print(S[0])
    else:
        ans = -1
        for i in range(N):
            for j in range(M):
                if S[i] == T[j]:
                    continue
                else:
                    ans = S[i]
                    break
            if ans != -1:
                break
        print(ans)

=======
Suggestion 3

def main():
    n,m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(m):
        if t[i] in s:
            print(-1)
            exit()
    for i in range(m):
        for j in range(n):
            if t[i] in s[j]:
                s[j] = s[j].replace(t[i], "_" * len(t[i]))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j]:
                print(-1)
                exit()
    ans = ""
    for i in range(n):
        ans += s[i] + "_"
    print(ans[:-1])

=======
Suggestion 4

def check(s):
    for t in T:
        if t == s:
            return False
    return True

=======
Suggestion 5

def isMatch(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if t[i] != '_' and s[i] != t[i]:
            return False
    return True

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]

    def check(s):
        for t in T:
            if t in s:
                return False
        return True

    def dfs(s):
        if len(s) == N:
            return s
        for i in range(N):
            if S[i] in s:
                continue
            if check(s + S[i]):
                ret = dfs(s + S[i])
                if ret != None:
                    return ret
        return None

    print(dfs(''))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]

    def check(x):
        for ti in t:
            if x.find(ti) >= 0:
                return False
        return True

    def dfs(i, x):
        if i == n:
            return x
        for j in range(i, n):
            if dfs(j + 1, x + s[j]) is not None:
                return x
        return None

    def solve():
        for i in range(n):
            x = dfs(i + 1, s[i])
            if x is not None and check(x):
                return x
        return None

    ans = solve()
    if ans is None:
        print(-1)
    else:
        print(ans)

=======
Suggestion 8

def check(s,t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if t[i] != '_' and s[i] != t[i]:
            return False
    return True

n,m = map(int,input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]

for i in range(1<<n):
    tmp = ''
    for j in range(n):
        if i & (1<<j):
            tmp += s[j] + '_'
        else:
            tmp += '_' + s[j]
    flag = True
    for j in range(m):
        if check(tmp,t[j]):
            flag = False
            break
    if flag:
        print(tmp)
        exit()
print(-1)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    S.sort()
    T.sort()
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                print(-1)
                exit()
    if N == 1:
        print(S[0])
        exit()
    else:
        if N == 2:
            print(S[0]+S[1])
            exit()
        else:
            if N == 3:
                print(S[0]+S[1]+S[2])
                exit()
            else:
                if N == 4:
                    print(S[0]+S[1]+S[2]+S[3])
                    exit()
                else:
                    if N == 5:
                        print(S[0]+S[1]+S[2]+S[3]+S[4])
                        exit()
                    else:
                        if N == 6:
                            print(S[0]+S[1]+S[2]+S[3]+S[4]+S[5])
                            exit()
                        else:
                            if N == 7:
                                print(S[0]+S[1]+S[2]+S[3]+S[4]+S[5]+S[6])
                                exit()
                            else:
                                if N == 8:
                                    print(S[0]+S[1]+S[2]+S[3]+S[4]+S[5]+S[6]+S[7])
                                    exit()

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    #print(S)
    #print(T)
    ans = ""
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if (S[i] + "_" + S[j]) not in T:
                ans = S[i] + "_" + S[j]
                break
            if ("_" + S[i] + "_" + S[j]) not in T:
                ans = "_" + S[i] + "_" + S[j]
                break
            if (S[i] + "_" + S[j] + "_") not in T:
                ans = S[i] + "_" + S[j] + "_"
                break
            if ("_" + S[i] + "_" + S[j] + "_") not in T:
                ans = "_" + S[i] + "_" + S[j] + "_"
                break
        if ans != "":
            break
    print(ans)
