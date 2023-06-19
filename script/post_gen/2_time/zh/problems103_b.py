Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if len(S) == len(T):
        for i in range(len(S)):
            S = S[1:] + S[0]
            if S == T:
                print("Yes")
                exit()
        print("No")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
    else:
        for i in range(len(S)):
            if S == T:
                print("Yes")
                break
            else:
                S = S[-1] + S[:-1]
        else:
            print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s in t+t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def check(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            return True
    return False

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if len(s) == len(t):
        for i in range(len(s)):
            if s == t:
                print('Yes')
                break
            s = s[-1] + s[0:-1]
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if len(s) == len(t):
        if t in (s + s):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 8

def rotate(s):
    return s[-1] + s[:-1]

s = input()
t = input()

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print('No')
        return
    for i in range(len(S)):
        if S == T:
            print('Yes')
            return
        S = S[-1] + S[:-1]
    print('No')

main()

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if (t in s+s):
        print("Yes")
    else:
        print("No")
