Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            if s == t:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print('No')
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print("No")
        return
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                print("No")
                return
        print("Yes")

=======
Suggestion 4

def main():
    s = input()
    t = input()

    if len(s) + 1 == len(t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def func(s,t):
    if len(s) > len(t):
        return "No"
    i = 0
    for j in range(len(t)):
        if i < len(s) and s[i] == t[j]:
            i += 1
    if i == len(s):
        return "Yes"
    else:
        return "No"

s = input()
t = input()

print(func(s,t))

=======
Suggestion 6

def isMatch(s, t):
    if len(s) > len(t):
        return False
    if s == t:
        return True
    if len(s) == 1:
        return False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s1 = s[0:i+1] + s[i+1:]
            if isMatch(s1, t):
                return True
    return False

s = input()
t = input()

=======
Suggestion 7

def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    s = len(S)
    t = len(T)
    if t < s:
        print("No")
        return
    if s == 2:
        if S[0] == S[1]:
            if S[0] == T[0]:
                print("Yes")
                return
            elif S[0] == T[1]:
                print("Yes")
                return
            else:
                print("No")
                return
        else:
            print("No")
            return
    if s == 3:
        if S[0] == S[1] == S[2]:
            if S[0] == T[0]:
                print("Yes")
                return
            elif S[0] == T[1]:
                print("Yes")
                return
            elif S[0] == T[2]:
                print("Yes")
                return
            else:
                print("No")
                return
        elif S[0] == S[1]:
            if S[0] == T[0]:
                if S[2] == T[1]:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            elif S[0] == T[1]:
                if S[2] == T[2]:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            else:
                print("No")
                return
        elif S[1] == S[2]:
            if S[1] == T[1]:
                if S[0] == T[0]:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            elif S[1] == T[2]:
                if S[0] == T[0]:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            else:
                print("No")
                return
        else:
            print("No")
            return
    if s == 4:
        if S[0] == S[1] == S[2] == S[3]:
            if S[0] == T[0]:
                print("Yes")
                return
            elif S[0] == T[1]:
                print

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    s = input()
    t = input()

    if len(s) + 1 != len(t):
        print("No")
        return

    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if len(S) == len(T) - 1:
        if S == T[:-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()
