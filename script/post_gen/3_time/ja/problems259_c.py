Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == len(s):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print("No")
        return
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(s):
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 3

def solve():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            if s == t:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 4

def solve():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    if S_len + 1 != T_len:
        print("No")
        return
    for i in range(S_len):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    if slen > tlen:
        print("No")
        exit()
    if slen == tlen:
        if s == t:
            print("Yes")
        else:
            print("No")
        exit()
    if slen < tlen:
        i = 0
        j = 0
        while i < slen:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == slen:
            print("Yes")
        else:
            print("No")
        exit()

=======
Suggestion 6

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len + 1 != t_len:
        print("No")
        return

    if s == t[:-1]:
        print("Yes")
        return

    print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            s = s[:i] + s[i-1] + s[i:]
            if s == t:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    if len(s) + 1 != len(t):
        print("No")
        exit()
    if s[0] != t[0]:
        print("No")
        exit()
    if s[-1] != t[-1]:
        print("No")
        exit()
    s = s[1:-1]
    t = t[1:-1]
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 9

def solve():
    S = input()
    T = input()

    if S == T:
        print("Yes")
        return

    s = S
    for i in range(len(S)):
        if s == T:
            print("Yes")
            return
        s = s[:i] + s[i] + s[i:]
    print("No")

=======
Suggestion 10

def solve(S,T):
    #print(S)
    #print(T)
    #print(len(S))
    #print(len(T))
    if len(S) < len(T):
        return False
    if S == T:
        return True
    if len(S) == len(T):
        return False
    if len(S) > len(T):
        if S[0:len(T)] == T:
            return True
        else:
            return solve(S[0:len(S)-1],T)
