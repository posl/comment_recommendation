Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print("Yes")
            break
        s = s[-1] + s[:-1]
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                print("No")
                break
        else:
            print("Yes")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        if s[i] == 'a':
            if t[i] == 'z':
                continue
            else:
                print("No")
                return
        if ord(s[i]) - ord(t[i]) == 1:
            continue
        else:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i:] + s[:i] == t:
                print("Yes")
                return
        print("No")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if t in s*2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve(S, T):
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            return True
    return False

=======
Suggestion 8

def main():
    s = input().rstrip()
    t = input().rstrip()
    if s == t:
        print("Yes")
        return
    for i in range(1, len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    
    for i in range(1, len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            return

    print("No")
