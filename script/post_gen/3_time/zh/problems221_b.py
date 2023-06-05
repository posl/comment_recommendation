Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        s = list(s)
        t = list(t)
        for i in range(len(s)-1):
            s[i], s[i+1] = s[i+1], s[i]
            if s == t:
                print("Yes")
                break
            s[i], s[i+1] = s[i+1], s[i]
        else:
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
            s = s[:i] + s[i+1] + s[i] + s[i+2:]
            if s == t:
                print("Yes")
                exit()
        print("No")

=======
Suggestion 3

def swap(i, j, s):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

s = input()
t = input()

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            if S[i] != T[i]:
                if S[i+1] == T[i] and S[i] == T[i+1]:
                    print("Yes")
                    exit()
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) == len(t):
        if s == t:
            print("Yes")
        else:
            for i in range(len(s) - 1):
                if s[i] == t[i+1] and s[i+1] == t[i]:
                    print("Yes")
                    break
            else:
                print("No")
    else:
        print("No")

=======
Suggestion 6

def swap(a, b):
    return b, a

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if len(S) == len(T) and len(S) >= 2 and len(S) <= 100 and len(T) >= 2 and len(T) <= 100:
        if S == T:
            print("Yes")
        else:
            S = list(S)
            T = list(T)
            for i in range(len(S)):
                for j in range(i+1, len(S)):
                    S[i], S[j] = S[j], S[i]
                    if S == T:
                        print("Yes")
                        break
                    else:
                        S = list(S)
                if S == T:
                    break
            if S != T:
                print("No")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s[0] == t[1] and s[1] == t[0] and len(s) == len(t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            s = list(s)
            s[i], s[i+1] = s[i+1], s[i]
            s = "".join(s)
            if s == t:
                print("Yes")
                break
            else:
                s = list(s)
                s[i], s[i+1] = s[i+1], s[i]
                s = "".join(s)
        else:
            print("No")

=======
Suggestion 10

def main():
    s = input()
    t = input()

    if s == t:
        print('Yes')
    else:
        for i in range(len(s) - 1):
            if s[:i] + s[i + 1] + s[i] + s[i + 2:] == t:
                print('Yes')
                break
        else:
            print('No')
