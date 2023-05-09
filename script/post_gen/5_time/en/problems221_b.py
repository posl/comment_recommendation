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
        print('Yes')
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                print('Yes')
                return
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        if s[i+1] == t[i] and s[i] == t[i+1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 4

def solve():
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
Suggestion 5

def swap(s, t):
    if s == t:
        return True
    for i in range(len(s) - 1):
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            return True
    return False

=======
Suggestion 6

def solve():
    s = input()
    t = input()
    if s==t:
        print("Yes")
        return
    for i in range(len(s)-1):
        if s[i+1]==t[i] and s[i]==t[i+1]:
            print("Yes")
            return
    print("No")
solve()

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(0, len(s)-1):
        if s[i] != t[i]:
            if s[i+1] == t[i] and s[i] == t[i+1]:
                print("Yes")
                return
            else:
                print("No")
                return
    print("No")
    return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return

    for i in range(len(S) - 1):
        if S[i] != T[i]:
            if S[i] == T[i + 1] and S[i + 1] == T[i]:
                print("Yes")
                return
            else:
                print("No")
                return
    print("No")
    return

=======
Suggestion 9

def solve():
    s = input()
    t = input()

    if s == t:
        print("Yes")
        return

    for i in range(len(s)-1):
        if s[i:i+2] == t[i:i+2][::-1]:
            print("Yes")
            return

    print("No")
