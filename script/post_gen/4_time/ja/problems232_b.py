Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        print("No")
        return
    for i in range(s_len):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(s_len):
        if s == t:
            print("Yes")
            return
        s = s[s_len-1] + s[0:s_len-1]
    print("No")
    return

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        if s[i] == t[i]:
            continue
        elif s[i] == t[i+1] and s[i+1] == t[i]:
            print("Yes")
            return
        else:
            print("No")
            return
    print("No")
    return

=======
Suggestion 9

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            if s[i] == 'z':
                if t[i] == 'a':
                    continue
                else:
                    print('No')
                    exit()
            elif s[i] == 'a':
                if t[i] == 'z':
                    continue
                else:
                    print('No')
                    exit()
            else:
                if s[i] < t[i]:
                    print('Yes')
                    exit()
                else:
                    print('No')
                    exit()
    print('Yes')
    exit()

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        exit()
    for i in range(1, len(S)):
        S = S[-1] + S[0:-1]
        if S == T:
            print('Yes')
            exit()
    print('No')
main()
