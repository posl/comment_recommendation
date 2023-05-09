Synthesizing 10/10 solutions

=======
Suggestion 1

def is_match(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i] and s[i] != '?':
            return False
    return True

=======
Suggestion 2

def check(s, t):
    for i in range(len(s)):
        if s[i] != '?' and t[i] != '?' and s[i] != t[i]:
            return False
    return True

s = input()
t = input()
for i in range(len(t)+1):
    s1 = s[:i] + t[i:]
    if check(s1, t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + t[i:] == s[:i] + t[i:]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + t[i:] == t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i]+t[i:] == s[:i]+t[i:]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    S = S.replace('?', 'a')
    T = T.replace('?', 'a')
    for i in range(len(S) - len(T) + 1):
        if S[i:i+len(T)] == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def solve(s,t):
    n = len(s)
    m = len(t)
    for i in range(n-m+1):
        for j in range(m):
            if s[i+j] != '?' and s[i+j] != t[j]:
                break
        else:
            return True
    return False

s = input()
t = input()
n = len(t)
for i in range(n+1):
    if solve(s[:i]+t+s[i:],t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    for i in range(tlen+1):
        if s[:i] == t[:i] and s[slen-tlen+i:] == t[i:]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    t_len = len(t)
    s_len = len(s)
    for i in range(t_len+1):
        if s[:i] + t_len - i + s[s_len - (t_len-i):] == t.replace('?', 'a'):
            print('Yes')
        else:
            print('No')

=======
Suggestion 10

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S.replace("?", "a")[:i] + S[i:len(S) - (len(T) - i)].replace("?", "a") == T:
            print("Yes")
        else:
            print("No")
