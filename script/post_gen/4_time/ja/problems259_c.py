Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    while len(s) < len(t):
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[:-1]
            t = t[::-1]
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    i = 0
    j = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            if s == t:
                print('Yes')
                return
    print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len > t_len:
        print('No')
        return
    if s == t[:s_len]:
        print('Yes')
        return
    print('No')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    if len(s) == len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[:i] == t[:i] and s[i+1:] == t[i:]:
                print("Yes")
                return
            else:
                print("No")
                return
    print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        exit()

    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            if S[:i+1]+S[i]+S[i+1:] == T:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 8

def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    if n >= m:
        print('No')
        return
    if s == t[:n]:
        print('Yes')
    else:
        print('No')

solve()

=======
Suggestion 9

def check(s, t):
    if s == t:
        return True
    if len(s) == len(t):
        return False
    if t[0] == t[1]:
        return check(s, t[1:])
    if t[-1] == t[-2]:
        return check(s, t[:-1])
    return check(s, t[1:-1])

s = input()
t = input()
print("Yes" if check(s, t) else "No")

=======
Suggestion 10

def is_ok(a,b):
    return a==b
