Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)+1):
        if s[:i] == t[:i] and s[i:] == t[i+1:]:
            print(i+1)
            break

=======
Suggestion 2

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            return
    print(len(s)+1)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans = i+1
            break
    if ans == 0:
        ans = len(s)+1
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            return
    print(len(s)+1)
    return

=======
Suggestion 7

def main():
    s = input()
    t = input()
    for i in range(len(s)+1):
        if s[:i] + s[i:] == t:
            print(i+1)
            return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    N = len(S)
    for i in range(N):
        if S[i] != T[i]:
            print(i+1)
            return
    print(N+1)

=======
Suggestion 9

def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    for i in range(len(S)+1):
        if S[:i] == T[:i] and S[i:] == T[i+1:]:
            print(i+1)
            break
