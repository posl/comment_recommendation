Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    cnt = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    T = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print(0)
        return
    if len(s) != len(t):
        print(-1)
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 7

def main():
    S = input()
    T = input()

    if S == T:
        print(0)
        return

    S = list(S)
    T = list(T)
    #print(S)
    #print(T)

    for i in range(len(S)):
        #print(i)
        if S == T:
            print(i)
            return
        else:
            S.append(S.pop(0))
            #print(S)

    print(-1)
    return
