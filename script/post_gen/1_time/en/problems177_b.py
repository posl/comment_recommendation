Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    ans = len(T)
    for i in range(len(S) - len(T) + 1):
        cnt = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ans = 1000
    for i in range(len(s) - len(t) + 1):
        cnt = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    ans = float("inf")
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = 10**9
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    min_change = 1001
    for i in range(len(s) - len(t) + 1):
        change = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                change += 1
        min_change = min(min_change, change)
    print(min_change)

main()

=======
Suggestion 6

def check(s,t):
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            return True
    return False

=======
Suggestion 7

def solve(s, t):
    sl = len(s)
    tl = len(t)
    res = 1000
    for i in range(sl - tl + 1):
        tmp = 0
        for j in range(tl):
            if s[i+j] != t[j]:
                tmp += 1
        res = min(res, tmp)
    return res

s = input()
t = input()
print(solve(s, t))

=======
Suggestion 8

def check(S,T):
    if (len(S) < len(T)):
        return False
    for i in range(len(S) - len(T)+1):
        for j in range(len(T)):
            if (S[i+j] != T[j]):
                break
        else:
            return True
    return False

=======
Suggestion 9

def get_input():
    S = input()
    T = input()
    return S, T
