Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
                return
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    s = list(s)
    t = list(t)
    for i in range(len(s)-1):
        s[i],s[i+1] = s[i+1],s[i]
        if s == t:
            print("Yes")
            return
        s[i],s[i+1] = s[i+1],s[i]
    print("No")
main()

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S) - 1):
        if S[i] == T[i + 1] and S[i + 1] == T[i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    s = list(s)
    t = list(t)
    for i in range(len(s)-1):
        s[i], s[i+1] = s[i+1], s[i]
        if s == t:
            print('Yes')
            return
        s[i], s[i+1] = s[i+1], s[i]
    print('No')
    return

=======
Suggestion 6

def solve(s, t):
    if s == t:
        return "Yes"
    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            return "Yes"
    return "No"

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S) - 1):
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)-1):
            if S[i] != T[i]:
                if S[i+1] == T[i] and S[i] == T[i+1]:
                    print('Yes')
                    return
        print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    else:
        for i in range(len(s)-1):
            s = s[:i] + s[i+1] + s[i] + s[i+2:]
            if s == t:
                print("Yes")
                return
            else:
                s = s[:i] + s[i+1] + s[i] + s[i+2:]
        print("No")
        return
