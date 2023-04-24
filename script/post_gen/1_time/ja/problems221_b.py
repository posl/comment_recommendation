Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                print("Yes")
                exit()
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                print("Yes")
                break
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
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print("Yes")
                exit()
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s) - 1):
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    S = list(S)
    T = list(T)
    for i in range(len(S) - 1):
        S[i], S[i + 1] = S[i + 1], S[i]
        if S == T:
            print("Yes")
            return
        S[i], S[i + 1] = S[i + 1], S[i]
    print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()

    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def main():
    s = input()
    t = input()
    flag = False
    if s == t:
        flag = True
    else:
        for i in range(len(s)-1):
            s = s[:i] + s[i+1] + s[i] + s[i+2:]
            if s == t:
                flag = True
                break
            else:
                s = s[:i] + s[i+1] + s[i] + s[i+2:]
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def check(s, t):
    for i in range(len(s)-1):
        if s[i] == t[i]:
            continue
        else:
            if s[i] == t[i+1] and s[i+1] == t[i]:
                return True
            else:
                return False
    return True

s = input()
t = input()
