Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i] == S[j]:
                print(-1)
                return

    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if T[i] == T[j]:
                print(-1)
                return

    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                print(-1)
                return

    for i in range(N):
        for j in range(M):
            if S[i] in T[j]:
                print(-1)
                return

    for i in range(M):
        for j in range(N):
            if T[i] in S[j]:
                print(-1)
                return

    for i in range(N):
        for j in range(M):
            if S[i] + '_' + T[j] not in T and T[j] + '_' + S[i] not in T:
                print(S[i] + '_' + T[j])
                return

main()

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(m):
                if t[k] == s[i] + '_' + s[j]:
                    print(t[k])
                    return
                if t[k] == s[j] + '_' + s[i]:
                    print(t[k])
                    return
    print(-1)

main()

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                print(-1)
                return
    for i in range(m):
        for j in range(i+1,m):
            if t[i] == t[j]:
                print(-1)
                return
    ans = ''
    for i in range(n):
        ans += s[i]
        if i < n-1:
            ans += '_'
    print(ans)

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j]:
                print(-1)
                return
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            if t[i] == t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if t[j] in s[i]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if '_' in t[j]:
                t[j] = t[j].replace('_', '')
    for i in range(n):
        for j in range(m):
            if t[j] in s[i]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if '_' in t[j]:
                t[j] = t[j].replace('_', '')
    for i in range(n):
        for j in range(m):
            if t[j] in s[i]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if '_' in t[j]:
                t[j] = t[j].replace('_', '')
    for i in range(n):
        for j in range(m):
            if t[j] in s[i]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(n):

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    if N == 1:
        if M == 0:
            print(S[0])
            return
        else:
            for t in T:
                if t == S[0]:
                    print(-1)
                    return
            print(S[0])
            return
    if M == 0:
        print(S[0])
        return
    for t in T:
        if t == S[0]:
            print(-1)
            return
    for t in T:
        if t == S[1]:
            print(-1)
            return
    if N == 2:
        print(S[0] + '_' + S[1])
        return
    if N == 3:
        print(S[0] + '_' + S[1] + '_' + S[2])
        return
    if N == 4:
        print(S[0] + '_' + S[2] + '_' + S[1] + '_' + S[3])
        return
    if N == 5:
        print(S[0] + '_' + S[2] + '_' + S[4] + '_' + S[1] + '_' + S[3])
        return
    if N == 6:
        print(S[0] + '_' + S[2] + '_' + S[4] + '_' + S[1] + '_' + S[3] + '_' + S[5])
        return
    if N == 7:
        print(S[0] + '_' + S[2] + '_' + S[4] + '_' + S[6] + '_' + S[1] + '_' + S[3] + '_' + S[5])
        return
    if N == 8:
        print(S[0] + '_' + S[2] + '_' + S[4] + '_' + S[6] + '_' + S[1] + '_' + S[3] + '_' + S[5] + '_' + S[7])
        return
solve()

=======
Suggestion 6

def check(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] != '_' and t[i] != '_' and s[i] != t[i]:
            return False
    return True

n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if check(s[i], s[j]):
            print(-1)
            exit()

for i in range(m):
    for j in range(m):
        if i == j:
            continue
        if check(t[i], t[j]):
            print(-1)
            exit()

for i in range(n):
    for j in range(m):
        if check(s[i], t[j]):
            print(-1)
            exit()

for i in range(n):
    for j in range(m):
        if check(t[j], s[i]):
            print(-1)
            exit()

for i in range(n):
    for j in range(m):
        if len(s[i]) + len(t[j]) > 16:
            continue
        for k in range(len(s[i])):
            if s[i][k:] + t[j] == t[j] + s[i][:k]:
                print(s[i][k:] + '_'*(16-len(s[i])-len(t[j])) + t[j])
                exit()
            if t[j][k:] + s[i] == s[i] + t[j][:k]:
                print(t[j][k:] + '_'*(16-len(s[i])-len(t[j])) + s[i])
                exit()

print(-1)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]

    def check(x):
        for i in range(m):
            if t[i] in x:
                return False
        return True

    def dfs(x):
        if len(x) == n:
            if check(x):
                print(x)
                exit()
            return

        for i in range(n):
            dfs(x + s[i])

    dfs("")

=======
Suggestion 8

def check(s1, s2, t):
    if len(s1) + len(s2) + len(t) - 2 < 3 or len(s1) + len(s2) + len(t) - 2 > 16:
        return False
    if t in s1 + s2:
        return False
    return True

=======
Suggestion 9

def main():
    pass
