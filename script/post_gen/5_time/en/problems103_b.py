Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
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
    else:
        print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()

    if S == T:
        print("Yes")
    else:
        for i in range(len(S)):
            S = S[len(S)-1] + S[:len(S)-1]
            if S == T:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S in T*2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s in t * 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    S = input()
    T = input()
    T2 = T + T
    if S in T2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def rotateString(s,t):
    for i in range(len(s)):
        if s == t:
            return True
        else:
            s = s[-1] + s[:-1]
    return False
