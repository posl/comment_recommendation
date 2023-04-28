Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if T in S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()

    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    s = input()
    t = input()
    if t in s:
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
    for i in range(s_len):
        if s[i:i+t_len] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def check(s, t):
    if len(s) < len(t):
        return False
    for i in range(len(s) - len(t) + 1):
        for j in range(len(t)):
            if s[i + j] != t[j]:
                break
        else:
            return True
    return False

s = input()
t = input()

=======
Suggestion 7

def main():
    S = input()
    T = input()
    s_len = len(S)
    t_len = len(T)
    if s_len < t_len:
        print("No")
        return
    for i in range(s_len - t_len + 1):
        if S[i:i+t_len] == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 8

def solve():
    s = input()
    t = input()
    if t in s:
        print('Yes')
    else:
        print('No')
solve()

=======
Suggestion 9

def check(S,T):
    if len(S)<len(T):
        return False
    for i in range(len(S)-len(T)+1):
        if S[i:i+len(T)]==T:
            return True
    return False

S=input()
T=input()
